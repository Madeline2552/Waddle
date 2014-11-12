#!/usr/bin/python

import cgi
import sqlite3
import cgitb
import Cookie
import os

cgitb.enable()

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

cookstring = os.environ.get('HTTP_COOKIE')
if cookstring:
	my_cookie = Cookie.SimpleCookie(cookstring)
	saved_session_id = my_cookie['session_id'].value
    
   
	c.execute('select * from users where session_id=?;', (saved_session_id,))

	all_results = c.fetchall()
	if len(all_results)==0:
		print "Content-type: application/json"
    		print
    		print '{"condition": false, "noCookie":false}'
		
	else:
		print "Content-type: application/json"
    		print
    		print '{"condition": true, "noCookie": false}'
		
	
else:
    print "Content-type: application/json"
    print
    print '{"condition": false, "noCookie": true}'
    

