#!/usr/bin/python

import cgi
import os
import Cookie
import sqlite3
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

un = form['un1'].value
pw = form['pw1'].value
em = form['em1'].value

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

c.execute('select * from users where name=?;', (un,))
all_results = c.fetchall()
if len(all_results)>0:
    message = "Sorry, it seems like someone already registered using this username or email"
else:
    message = "wahoo!"
    c.execute('insert into users values(?, ? ,?, ?);', (un, pw, em, ""))
    conn.commit()


print "Content-type: text/html"
print

print "<html>"
print "<head><title>Registration</title></head>"
print "<body>"
print "<h1>" +message+"</h1>"
print "<h2>your username is: " + un + " </h2>"
print "<a href='../cgi-bin/home.py'> Back to Main Page </a>"

print "<pre>"

for row in c.execute('select * from users'):
    print 'username: ', row[0], '| email: ', row[2]
    
c.close()
print "</pre>"
print "</body>"
print "</html>"
