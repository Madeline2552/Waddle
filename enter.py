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
t = form['time'].value
theTime = time.time()
unixTime = round(theTime, 0)
inputTime = time.strftime("%a, %d-%b-%Y %T EST", time.localtime(theTime+7200))

conn = sqlite3.connect('time.db')
c = conn.cursor()

c.execute('insert into timeData values(?, ?, ?, ?);', (loc,t, inputTime, unixTime))
conn.commit()

theInput = {
    "loc": loc,
    "time": t,
    "inputTime": inputTime
}
c.close()
print "Content-type: application/json"
# don't forget the extra newline!
print
print json.dumps(theInput)
