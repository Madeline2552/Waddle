#!/usr/bin/python
import cgi
import sqlite3
import cgitb
import Cookie
import os
import uuid
import time



cgitb.enable()
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

form = cgi.FieldStorage()
pw1 = form["u_n"].value
pw2 = form["p_w"].value

cookstring = os.environ.get('HTTP_COOKIE')
my_cookie = Cookie.SimpleCookie(cookstring)
#session_id = str(uuid.uuid4())
saved_session_id = my_cookie['session_id'].value
	
c.execute("select * from users where session_id=? and pass=?;", (saved_session_id, pw1,))
rightPassword = c.fetchall()
if pw1==pw2 and (len(rightPassword)>0):
	expires = time.time() - 14*24*3600
	
	my_cookie['session_id'] = ' '
	my_cookie['session_id']['expires'] = time.strftime("%a, %d-%b-%Y %T GMT", time.gmtime(expires))

	for row in c.execute('select name from users where session_id is ?;',(saved_session_id,)):
		name = row[0]
	c.execute('delete from users where session_id=?;', (saved_session_id,))
	conn.commit()

	print "Content-type: text/html"
	print my_cookie
	print 

	print"<html>"
	print"<head><title> "
	print "We are sorry to see you go!</title></head>"
	print"<body>"
	print"<h1> <center>We are sorry to see you go,"
	print name + "!"
	print"<br>This account has been deleted. </h1>"
	print "<a href='../index.html'> <center> Back to Main Page</center> </a> </center>"
	print"</body>"
	print"</html>"
else:
	print "Content-type: text/html"
	print 

	print"<html>"
	print"<head><title>Wrong password(s)</title></head>"
	print"<body>"
	print"<h1> ThisJSDJKFHKSDFKJSDfhkdhkfsd. </h1>"
	print "<a href='../index.html'> Back to Main Page </a>"
	print"</body>"
	print"</html>"
