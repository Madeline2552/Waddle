#!/usr/bin/python

import json
import sqlite3
import cgi
import os
import cgitb



cgitb.enable()

form = cgi.FieldStorage()
loc = form['l'].value

conn = sqlite3.connect('time.db')

cursor = conn.cursor()
cursor.execute("select * from timeData where location is ?;", (loc,))
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


