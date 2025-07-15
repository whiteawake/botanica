#!/usr/bin/env python

print "Content-Type: text/html\n"

import sqlite3, sys, cgi, csv
import cgitb; cgitb.enable()

print("""
<!DOCTYPE html>
<html>
<head>
	<title>Location - Botanica</title>
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
	<h2 class="descript">Plants by Location</h2>
		<table>
			<thead>
				<tr>
					<th>Location</th>
					<th>Common name</th>
					<th>Scientific name</th>
					<th>Family</th>
					<th>Weather Comments</th>
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

my_data = db.execute('SELECT * FROM Plants ORDER BY column_3')


alt_database = "locations.db"
alt_file = "locations.txt"

adb = sqlite3.connect(alt_database)
adb.row_factory = sqlite3.Row

adb.execute("DROP TABLE IF EXISTS Locations")
adb.execute("CREATE TABLE Locations(alt_column_1 TEXT, alt_column_2 TEXT);")

alt_reader = csv.reader(open(alt_file, 'r'), delimiter='|')
for row in alt_reader:
	alt_data = [unicode(row[0], "utf8"), unicode(row[1], "utf8")]
	adb.execute("INSERT INTO Locations(alt_column_1, alt_column_2) VALUES (?, ?);", alt_data)

adb.commit()

alt_data = adb.execute('SELECT * FROM Locations ORDER BY alt_column_2')

def weather():
	for row in alt_data:
		return(row['alt_column_2'])

for row in my_data:
	weather_result = weather()
	print("""
				<tr>
					<td><strong>""" + row['column_3'] + """</strong></td>
					<td>""" + row['column_1'] + """</td>
					<td><em>""" + row['column_2'] + """</em></td>
					<td><em>""" + row['column_4'] + """</em></td>
					<td>""" + str(weather_result) + """</td>
				</tr>
		""")
print("""
	</tbody></table></div>
	<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js'></script>	
	<script src="resources/javascript/impress.js"></script>
	</body></html>
	""")