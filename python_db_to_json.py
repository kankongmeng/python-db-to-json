import pyodbc
import json
import collections
import sqlite3

# For connecting to cloud db server
#connstr = 'DRIVER={SQL Server};SERVER=ServerName;DATABASE=database;'
#conn = pyodbc.connect(connstr)

# For connecting local db file
conn = sqlite3.connect('C:\Python27\database.db')
cursor = conn.cursor()

cursor.execute("""
            SELECT description, author
            FROM Books
            WHERE author = 'kelvin';
            """)
colnames = cursor.description
for row in colnames:
  print row[0]
rows = cursor.fetchall()

# Convert query to row arrays
rowarray_list = []
for row in rows:
    t = (row[0], row[1])
    rowarray_list.append(t)
 
j = json.dumps(rowarray_list)

rowarrays_file = 'rowarrays.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
objects_list = []

# Process result to designed json property
for row in rows:
    d = collections.OrderedDict()
    d['category'] = "motivation"
    d['author'] = row[1]
    d['content'] = row[0]
    objects_list.append(d)

j = json.dumps(objects_list)

# Go get uou json data from objects.js file
objects_file = 'objects.js'
f = open(objects_file,'w')
print >> f, j
 
conn.close()