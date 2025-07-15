#!/usr/bin/python
print 'Content-type: text/html\n\n'

import sqlite3, sys, cgi
import cgitb; cgitb.enable()

print("""
	<!DOCTYPE html>
	<html>
	<head>
		<title>Create - Botanica</title>
		<meta name="author" content="Asha" />
		<meta charset="UTF-8" />
		<link rel="stylesheet" type="text/css" href="resources/css/mainstyle.css" />
		<link rel="stylesheet" type="text/css" href="resources/css/neostyle.css" />
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
			<h1 class='insetshadow' style="margin-left: -15px;">Create a New Database</h1>
			<div id="container">
			<div id="message" style="margin-left: -320px;">
					<a class="message" style=" margin-top: 10px; margin-left: 20px;" id="animate" href="home.py">Home</a>
				</div>
			</div>
    	</div>
    	<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js'></script>
		<script src="resources/javascript/impress.js"></script>
		<script src="resources/javascript/neotext_create.js"></script>
	</body>
	</html>
	""")

plants_database = "plants.db"
plants_file = "plants.txt"
locations_database = "locations.db"
locations_file = "locations.txt"
family_file = "families.txt"

pdb = sqlite3.connect(plants_database)
plant_cursor = pdb.cursor()
ldb = sqlite3.connect(locations_database)
location_cursor = ldb.cursor()

plant_cursor.execute("""DROP TABLE IF EXISTS Plants""")
location_cursor.execute("""DROP TABLE IF EXISTS Locations""")

plant_cursor.execute("""CREATE TABLE Plants (column_1 TEXT, 
										column_2 TEXT, 
										column_3 TEXT, 
										column_4 TEXT, 
										column_5 TEXT);
				""")

location_cursor.execute("""CREATE TABLE Locations (column_1 TEXT, 
										column_2 TEXT);
				""")
open(family_file, 'w').close()
open(locations_file, 'w').close()
open(plants_file, 'w').close()
pdb.commit()
ldb.commit()
plant_cursor.close()
location_cursor.close()
