#!/usr/bin/python

import json
import sqlite3
import cgi
import os
import cgitb



cgitb.enable()

form = cgi.FieldStorage()
loc = form['l'].value
past = form['past'].value
future = form['future'].value
dayOfWeek = form['dayOfWeek'].value
#timeNow = form['timeNow'].value
conn = sqlite3.connect('time.db')

cursor = conn.cursor()
#cursor.execute("select * from timeData where location is ? and unix between ? and ?;", (loc, past, future,))
#rows = [x for x in cursor]
#cols = [x[0] for x in cursor.description]
#info = []
#
#for row in rows:
#        infri = {}
#        for prop, val in zip(cols, row):
#                infri[prop] = val
#        info.append(infri)
#infoJson = json.dumps(info)

cursor.execute("select * from timeData where trim(substr(inputTime,1,3)) is ? and location is ? and trim(substr(inputTime,18,5)) < ? and trim(substr(inputTime,18,5)) > ?", (dayOfWeek, loc, future, past))
rows = [x for x in cursor]
cols = [x[0] for x in cursor.description]
info = []

for row in rows:
    infri = {}
    for prop, val in zip(cols, row):
        infri[prop] = val
    info.append(infri)
infoJson = json.dumps(info)


cursor.close()

print "Content-type: application/json"
print
print infoJson


