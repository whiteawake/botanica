#!/usr/bin/env python

print "Content-Type: text/html\n"

import sqlite3, sys, cgi, csv
import cgitb; cgitb.enable()
from db_functions import *

print("""
<!DOCTYPE html>
<html>
<head>
	<title>First 10 - Botanica</title>
	<meta name="author" content="Asha" />
	<meta charset="UTF-8" />
	<link rel="stylesheet" type="text/css" href="resources/css/mainstyle.css" />
	<link rel="icon" href="resources/images/tree.png" type="image/x-icon">  
	<script type="text/javascript" src='http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js'></script>
	<script type="text/javascript" src="resources/javascript/prefixfree.min.js"></script>
</head>
<body>
	<div class="navcont">
			<div class="nav">
				<ul>
					<li class="drop">
	            		<a href="home.py">Database</a>
            			<div class="dropdownContain">
							<div class="dropOut">
								<ul>
									<li><a href="create.py">Create new</a></li>
								</ul>
								<ul>
									<li><a href="insert.py">Insert data</a></li>
								</ul>
							</div>
						</div>
					</li>
					<li class="drop">
	            		<a href="#">Query</a>
            			<div class="dropdownContain">
							<div class="dropOut">
								<ul>
									<li><a href="first_10.py">First 10</a></li>
								</ul>
								<ul>
									<li><a href="starting.py">Starting with..</a></li>
								</ul>
								<ul>
									<li><a href="from.py">Plants from..</a></li>
								</ul>
							</div>
						</div>
					</li>              
				<li class="drop">
	            		<a href="#">Plants</a>
            			<div class="dropdownContain">
							<div class="dropOut">
								<ul>
									<li><a href="database.py">All</a></li>
								</ul>
								<ul>
									<li><a href="by_location.py">By Location</a></li>
								</ul>
								<ul>
									<li><a href="by_family.py">By Family</a></li>
								</ul>
							</div>
						</div>
					</li>
					<li class="drop">
	            		<a href="#">Add</a>
            			<div class="dropdownContain">
							<div class="dropOut">
								<ul>
									<li><a href="plants.py">Plants</a></li>
								</ul>
								<ul>
									<li><a href="location.py">Location</a></li>
								</ul>
								<ul>
									<li><a href="family.py">Family</a></li>
								</ul>
							</div>
						</div>
					</li>
				</ul>
			</div>
		</div>
	<div id="formContainer">
	<h2 class="descript">First 10 Plants</h2>
		<table>
			<thead>
				<tr>
					<th>Common name</th>
					<th>Scientific name</th>
					<th>Location</th>
					<th>Family</th>
					<th>Comments</th>
				</tr>
			</thead>
			<tbody>
			""")
my_database = "plants.db"
my_file = "plants.txt"

db = sqlite3.connect(my_database)
db.row_factory = sqlite3.Row

db.execute("DROP TABLE IF EXISTS Plants")
db.execute("CREATE TABLE Plants(column_1 TEXT, column_2 TEXT, column_3 TEXT, column_4 TEXT, column_5 TEXT);")

reader = csv.reader(open(my_file, 'r'), delimiter='|')
for row in reader:
	my_data = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8"), unicode(row[3], "utf8"), unicode(row[4], "utf8")]
	db.execute("INSERT INTO Plants(column_1, column_2, column_3, column_4, column_5) VALUES (?, ?, ?, ?, ?);", my_data)

db.commit()

my_data = db.execute("""SELECT * FROM Plants LIMIT 10""")

for row in my_data:
	print("""
				<tr>
					<td><strong>""" + row['column_1'] + """</strong></td>
					<td><em>""" + row['column_2'] + """</em></td>
					<td>""" + row['column_3'] + """</td>
					<td>""" + row['column_4'] + """</td>
					<td>""" + row['column_5'] + """</td>
				</tr>
		""")
print("""
	</tbody></table>
	<br /><br />
	<h2 class="descript">First 10 Locations</h2>
		<table>
				<thead>
					<tr>
						<th>Location</th>
						<th>Comments</th>
					</tr>
				</thead>
				<tbody>
	""")

location_database = "locations.db"
location_file = "locations.txt"

ldb = sqlite3.connect(location_database)
ldb.row_factory = sqlite3.Row

ldb.execute("DROP TABLE IF EXISTS Locations")
ldb.execute("CREATE TABLE Locations(column_1 TEXT, column_2 TEXT);")

reader = csv.reader(open(location_file, 'r'), delimiter='|')
for row in reader:
	location_data = [unicode(row[0], "utf8"), unicode(row[1], "utf8")]
	ldb.execute("INSERT INTO Locations(column_1, column_2) VALUES (?, ?);", location_data) #3rd column to be number of plants

ldb.commit()
location_data = ldb.execute("""SELECT * FROM Locations LIMIT 10""")

for row in location_data:
	print("""
				<tr>
					<td><strong>""" + row['column_1'] + """</strong></td>
					<td>""" + row['column_2'] + """</td>
				</tr>
		""")
print("""
	</tbody></table>
	<br /><br />
	<h2 class="descript">First 10 Families</h2>
		<table>
				<thead>
					<tr>
						<th>Family</th>
					</tr>
				</thead>
				<tbody>
	""")

family_database = "families.db"
family_file = "families.txt"

fdb = sqlite3.connect(family_database)
fdb.row_factory = sqlite3.Row
plant_cursor = db.cursor()

fdb.execute("DROP TABLE IF EXISTS Families")
fdb.execute("CREATE TABLE Families(column_1 TEXT);")

reader = csv.reader(open(family_file, 'r'), delimiter='|')
for row in reader:
	family_data = [unicode(row[0], "utf8")]
	fdb.execute("INSERT INTO Families(column_1) VALUES (?);", family_data) #2nd column to be number of plants

fdb.commit()
family_data = fdb.execute("""SELECT * FROM Families LIMIT 10""")

plant_cursor.execute('''SELECT COUNT(column_1) FROM Plants
			    WHERE column_1 LIKE column_4''')

records = plant_cursor.fetchall()

for row in family_data:
	print("""
				<tr>
					<td><strong>""" + row['column_1'] + """</strong></td>
				</tr>
		""")

print("""
	</tbody></table></div>
	<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js'></script>	
	<script src="resources/javascript/impress.js"></script>
	</body></html>
	""")