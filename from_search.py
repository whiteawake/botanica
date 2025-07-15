#!/usr/bin/env python

print "Content-Type: text/html\n"

import sqlite3, sys, cgi, csv
import cgitb; cgitb.enable()
from db_functions import *
form = cgi.FieldStorage()

print("""
<!DOCTYPE html>
<html>
<head>
	<title>From - Botanica</title>
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
	""")

plant_database = 'plants.db'
pdb = sqlite3.connect(plant_database)
plant_cursor = pdb.cursor()

form = cgi.FieldStorage()
location = form.getvalue('from_location')
values = { "column_3": location }

print('<h1>Plants from ' + str(location) + '</h1>')
plant_cursor.execute('''SELECT column_3, COUNT(column_1) FROM Plants
			    WHERE column_3 = :column_3
			    GROUP BY column_3''', values)

records = plant_cursor.fetchall()
if(len(records) == 0):
    print('There are no plants from ' + str(location))
else:
    print('There are ' + str(records[0][1]) + ' plants from ' + records[0][0])
print('<br /><br />')
print('The plants from ' + str(location) + ' are:<br />')

plant_cursor.execute('''SELECT column_1, column_2, column_3
		    FROM Plants
		    WHERE column_3 = :column_3''', values)
fields = ["Registration", "Last Name", "First Name"]
records = plant_cursor.fetchall()
print_Records(records)

pdb.commit()
plant_cursor.close()

print("""
	</div>
	<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js'></script>	
	</body></html>
	""")