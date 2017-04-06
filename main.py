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
        <a href="/">Signup</a>
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    def get(self):
       

        # a form for adding new movies
        user_form = """
        <form action="/add" method="post">
            <label>
                Username
                <input type="text" name="user_name"/>
                
            </label></br>
        <form action="/add" method="post">
            <label>
                Password
                <input type="text" name="password"/>
            </label><br>
        <form action="/add" method="post">
            <label>
                Password (confirm)
                <input type="text" name="confirm"/>
            </label><br>
            <input type="submit" value="Submit"/>
        </form>
        """
        self.response.write(user_form)
        
        


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
