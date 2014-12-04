#!/usr/bin/python
import cgi
import os
import sqlite3
import cgitb
import Cookie
import os
import time
import json
cgitb.enable()

form = cgi.FieldStorage()

loc = form['loc'].value
count=0;

conn2 = sqlite3.connect('accounts.db')
c2 = conn2.cursor()

cookstring = os.environ.get('HTTP_COOKIE')
my_cookie = Cookie.SimpleCookie(cookstring)
saved_session_id = my_cookie['session_id'].value
if(loc == "Starbucks"):
    c2.execute('select Starbucks from users where session_id=?;',(saved_session_id,))
    count = c2.fetchone()[0]+1
    c2.execute('update users set starbucks = ? where session_id=?;', (count, saved_session_id,))
if(loc == "Connections"):
    c2.execute('select connections from users where session_id=?;',(saved_session_id,))
    count = c2.fetchone()[0]+1
    c2.execute('update users set connections = ? where session_id=?;', (count, saved_session_id,))
if(loc == "PV"):
    c2.execute('select puravida from users where session_id=?;',(saved_session_id,))
    count = c2.fetchone()[0]+1
    c2.execute('update users set puravida = ? where session_id=?;', (count, saved_session_id,))
if(loc == "Postoffice"):
    c2.execute('select postoffice from users where session_id=?;',(saved_session_id,))
    count = c2.fetchone()[0]+1
    c2.execute('update users set postoffice = ? where session_id=?;', (count, saved_session_id,))
if(loc == "Chipotle"):
    c2.execute('select chipotle from users where session_id=?;',(saved_session_id,))
    count = c2.fetchone()[0]+1
    c2.execute('update users set chipotle = ? where session_id=?;', (count, saved_session_id,))


conn2.commit()
c2.close()

print "Content-type: text/html"
# don't forget the extra newline!
print
print count

