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
    return username and USER_RE.match(username)
    
PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return email or EMAIL_RE.match(email) 
    

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        Signup
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""
user_form = """
        <form method="post">
            <table>
            <tr>
            <td class="label">
                Username
            </td>
            <td>
                <input type="text" name="username" value="username">
            </td>
            </tr>
            <table>
            <tr>
            <td class="label">
                Password
            </td>
            <td>
                <input type="text" name="password" value="">
            </td>
            </tr>
            <table>
            <tr>
            <td class="label">
                Verify Password
            </td>
            <td>
                <input type="text" name="verify" value="">
            </td>
            </tr>
            <table>
            <tr>
            <td class="label">
                Email (optional)
            </td>
            <td>
                <input type="text" name="email" value="email">
            </td>
            </tr>
            </table>
            <input type="submit" value="Submit"/>
        </form>
        """
class Index(webapp2.RequestHandler):
    
    def write_form(self, error=""):
        self.response.write(user_form % {"error": error})
    
    def get(self):
       

        
        
        self.write_form()
        
    def post(self):
        user_username = valid_username(self.request.get('username'))
        user_password = valid_password(self.request.get('password'))
        user_validate = valid_password(self.request.get('password'))
        user_email = valid_email(self.request.get('email'))
        
        if not user_username:
            self.write_form("That is not a valid Username.")
        
        
        
        


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
