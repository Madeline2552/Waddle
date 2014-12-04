#!/usr/bin/python

import json
import sqlite3
import cgi
import os
import cgitb
import Cookie


cgitb.enable()
form = cgi.FieldStorage()

conn = sqlite3.connect('accounts.db')
cursor = conn.cursor()

oldpass = form['oldpass'].value
newpass1 = form['newpass1'].value


cookstring = os.environ.get('HTTP_COOKIE')
my_cookie = Cookie.SimpleCookie(cookstring)
saved_session_id = my_cookie['session_id'].value

cursor.execute('select pass from users where session_id=?;',(saved_session_id,))
passCheck = cursor.fetchone()[0]

if passCheck == oldpass:
    cursor.execute('update users set pass=? where session_id=? and pass=?;', (newpass1, saved_session_id, oldpass,))
    conn.commit()
    print "Content-type: application/json"
    print
    print '{"condition": true}'
else:
    print "Content-type: application/json"
    print
    print '{"condition": false}'

cursor.close()
