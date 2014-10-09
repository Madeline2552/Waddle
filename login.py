#!/usr/bin/python

import cgi
import sqlite3
import cgitb
import Cookie
import os
import uuid

cgitb.enable()

form = cgi.FieldStorage()
un = form['u_n'].value
pw = form['p_w'].value

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

cookstring = os.environ.get('HTTP_COOKIE')
if cookstring:
    my_cookie = Cookie.SimpleCookie(cookstring)
    saved_session_id = my_cookie['session_id'].value
    
    
    c.execute('select * from users where name=? and pass=? and session_id=?;', (un, pw, saved_session_id))

    all_results = c.fetchall()
    if len(all_results)==0:
        print "Content-type: text/html"
        print
        
        print "<html>"
        print "<head><title>WRONG PASSWORD OR USERNAME!!llll!</title></head>"
        print "<body>"
        print "<h1>You're not in!</h1>"
        print "<h2>You have the wrong password or username (or you are already logged in as someone else):^(</h2>"
        print "<pre>"
    else:
        print "Content-type: text/html"
        print
        
        print "<html>"
        print "<head><title>You're already in!</title></head>"
        print "<body>"
        print "<h1>Dope. You're already logged in, "+ un +"</h1>"
        print "<h2>Here's a list of some registered users</h2>"
        print "<pre>"

    for row in c.execute('select * from users'):
        print 'username: ', row[0], '| email: ', row[2], '| cookie?: ', row[3]
else:
    c.execute('select * from users where name=? and pass=?;', (un, pw))
    all_results = c.fetchall()
    if len(all_results)==0:
        print "Content-type: text/html"
        print
            
        print "<html>"
        print "<head><title>WRONG PASSWORD OR USERNAME!!!!!!!</title></head>"
        print "<body>"
        print "<h1>You're not in.</h1>"
        print "<h2>You have the wrong password or username :^(</h2>"
        print "<pre>"
    else:
        #first time logging in
        session_id = str(uuid.uuid4())
        c.execute('update users set session_id=? where name=?',(session_id, un))
        conn.commit()
        cook = Cookie.SimpleCookie()
        cook['session_id'] = session_id
        print "Content-type: text/html"
        print cook
        print
    
        print "<html>"
        print "<head><title>It's your first time logging in!</title></head>"
        print "<body>"
        print "<h1>Nice! It's your first time logging in!</h1>"
        print "<h2>Here's a list of some registered users</h2>"
        print "<pre>"



        for row in c.execute('select * from users'):
            print 'username: ', row[0], '| email: ', row[2], '| cookie?: ', row[3]

print "</pre>"
print "</body>"
print "</html>"
