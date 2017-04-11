#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

import cgi

import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)
    
PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return EMAIL_RE.match(email) 
    
def escape_html(s):
    return cgi.escape(s, quote=True)
# html boilerplate for the top of every page

user_form = """
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
            <td class="label">
                Username
            </td>
            <td>
                <input type="text" name="username" value="%(username)s">
            </td>
            <td class="error">
                %(username_error)s
            </td>
        </tr>
 
        <tr>
            <td class="label">
                Password
            </td>
            <td>
                <input type="password" name="password" value="%(password)s">
            </td>
            <td class="error">
                %(password_error)s
            </td>
        </tr>
 
        <tr>
            <td class="label">
            Verify Password
            </td>
            <td>
                <input type="password" name="verify" value="%(verify)s">
            </td>
            <td class="error">
                %(verify_error)s
            </td>
        </tr>
 
        <tr>
            <td class="label">
                Email (optional)
            </td>
            <td>
                <input type="text" name="email" value="%(email)s">
            </td>
            <td class="error">
                %(email_error)s
            </td>
        </tr>
      </table>
 
      <input type="submit">
    </form>
  
"""
class Index(webapp2.RequestHandler):
    
    def write_form(self, username="", password="", verify="", email="", username_error="", password_error="", verify_error="", email_error=""):
        self.response.write(user_form % {"username" : username,
                                                "password" : password,
                                                "verify" : verify,
                                                "email" : email,
                                                "username_error" : username_error,
                                                "password_error" : password_error,
                                                "verify_error" : verify_error,
                                                "email_error" : email_error})
 

    def get(self):
    
        self.write_form()
        
    def post(self):
        user_username = self.request.get('username')
        user_password = self.request.get('password')
        user_verify = self.request.get('verify')
        user_email = self.request.get('email')
        
        username=valid_username(user_username)
        password=valid_password(user_password)
        verify=valid_password(user_verify)
        email=valid_email(user_email)
        
        esc_username = escape_html(user_username)
        esc_password = escape_html(user_password)
        esc_verify = escape_html(user_verify)
        esc_email = escape_html(user_email)
 
        username_error = ""
        password_error = ""
        verify_error = ""
        email_error = ""
 
        
 
        if not valid_username(user_username):
            username_error = "That is not a valid username."
            
            
        if not valid_password(user_password):
            password_error = "That is not a valid password."
            
 
        if not user_password == user_verify:
            verify_error = "Your passwords do not match!"
            
        
        if user_email=="":
            email=""
            
        
        elif not valid_email(user_email):
            email_error = "That is not a valid email address."
            
        
        
        
        if username_error!="" or password_error!="" or verify_error!="" or email_error!="":
            self.write_form(esc_username, esc_password, esc_verify, esc_email, username_error, password_error, verify_error, email_error)
           
            
        else:
             
            
            self.redirect("/welcome?username=%s" % user_username)
class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        self.response.write("Welcome! %s" % username)
 
            
        
        
        
        


app = webapp2.WSGIApplication([
    ('/', Index), 
    ('/welcome', WelcomeHandler)
], debug=True)
