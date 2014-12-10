#!/usr/bin/python
import cgi
import sqlite3
import cgitb
import Cookie
import os
import uuid
import time

cgitb.enable()


expires = time.time() - 14*24*3600
#cookstring = os.environ.get('HTTP_COOKIE')

my_cookie = Cookie.SimpleCookie()
#session_id = str(uuid.uuid4())
#saved_session_id = my_cookie['session_id'].value
my_cookie['session_id'] = ' '
my_cookie['session_id']['expires'] = time.strftime("%a, %d-%b-%Y %T GMT", time.gmtime(expires))



print "Content-type: text/html"
print my_cookie
print 

print"<html>"
print"<head><title> Waddling Out!</title></head>"
print"<body>"
print"<h1> You are now logged out. Thank you for visiting.</h1>"
print "<a href='../index.html'> Back to Main Page </a>"
print"</body>"
print"</html>"
