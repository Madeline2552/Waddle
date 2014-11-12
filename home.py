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

		print 'Content-Type: text/html'
		print 'Location: http://ztiet.rochestercs.org/index.html'		
		print # HTTP says you have to have a blank line between headers and content
		print '<html>'
		
		print '<head>'
		print '<meta http-equiv="refresh" content="0;url= http://ztiet.rochestercs.org/index.html" />' 
		print '    <title>You are going to be redirected</title>'
		print '  </head>' 
		print '  <body>'
		print '    Redirecting... <a href="http://ztiet.rochestercs.org/index.html">Click here if you are not redirected</a>' 
		print '  </body>'
		print '</html>'
		
	else:

		print 'Content-Type: text/html'
		print "Location: http://ztiet.rochestercs.org/home.html"
		print # HTTP says you have to have a blank line between headers and content
		print '<html>'
		
		print '<head>'
		print '<meta http-equiv="refresh" content="0;url= http://ztiet.rochestercs.org/home.html" />'
		print '    <title>You are going to be redirected</title>'
		print '  </head>' 
		print '  <body>'
		print '    Redirecting... <a href="http://ztiet.rochestercs.org/home.html">Click here if you are not redirected</a>'
		print '  </body>'
		print '</html>'
		
		

else:

	print 'Content-Type: text/html'
	print 'Location:  http://ztiet.rochestercs.org/index.html'
	print # HTTP says you have to have a blank line between headers and content
	print '<html>'
		
	print '<head>'
	print '<meta http-equiv="refresh" content="0;url= http://ztiet.rochestercs.org/index.html" />' 
	print '    <title>You are going to be redirected</title>'
	print '  </head>' 
	print '  <body>'
	print '    Redirecting... <a href="http://ztiet.rochestercs.org/index.html">Click here if you are not redirected</a>' % redirectURL
	print '  </body>'
	print '</html>'
