#!/usr/bin/python

print("Content-Type: text/html\n")

import sqlite3, sys, cgi, csv
import cgitb; cgitb.enable()

print("""
	<!DOCTYPE html>
	<html>
	<head>
		<title>Plants - Botanica</title>
		<meta name="author" content="Asha" />
		<meta charset="UTF-8" />
		<link rel="stylesheet" type="text/css" href="resources/css/mainstyle.css" />
		<link rel="icon" type="image/x-icon" href="resources/images/tree.png" />  
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
		<br />
		<br />
		<div id="formContainer">
			<h1 class='insetshadow' style="margin-left: -15px;">Plants</h1>
			<form method="post" action="engine.py">  
				<div class="formItem">
					<label for="name">eg. Jarrah</label>
					<input type="text" placeholder="Common name" id="name" name="name" required />
        		</div>
        		<div class="formItem">
	        		<label for="binom">eg. <em>Eucalyptus marginata</em></label>
        			<input type="binom" placeholder="Scientific name" id="binom" name="binom" required />
        		</div>
        		<label class="location">
      				<select name="location">
        				<option selected>- Location -</option>
    """)

my_database = "locations.db"
my_file = "locations.txt"

db = sqlite3.connect(my_database)
db.row_factory = sqlite3.Row

db.execute("DROP TABLE IF EXISTS Locations")
db.execute("CREATE TABLE Locations(column_1 TEXT, column_2 TEXT);")

reader = csv.reader(open(my_file, 'r'), delimiter='|')
for row in reader:
	my_data = [unicode(row[0], "utf8"), unicode(row[1], "utf8")]
	db.execute("INSERT INTO Locations(column_1, column_2) VALUES (?, ?);", my_data)

db.commit()

my_data = db.execute('SELECT * FROM Locations ORDER BY column_1')

for row in my_data:
	print("<option value="+ row['column_1'] +">"+ row['column_1'] +"</option>")

print("""
      				</select>
        		</label>
        		<label class="family">
      				<select name="family"><option selected>- Family -</option>
    """)
family_database = "families.db"
family_file = "families.txt"

db = sqlite3.connect(family_database)
db.row_factory = sqlite3.Row

db.execute("DROP TABLE IF EXISTS Families")
db.execute("CREATE TABLE Families(column_1 TEXT);")

reader = csv.reader(open(family_file, 'r'), delimiter='|')
for row in reader:
	my_data = [unicode(row[0], "utf8")]
	db.execute("INSERT INTO Families(column_1) VALUES (?);", my_data)

db.commit()

my_data = db.execute('SELECT * FROM Families ORDER BY column_1')

for row in my_data:
	print("<option value="+ row['column_1'] +">"+ row['column_1'] +"</option>")

print("""
      				</select>
        		</label>
        		<div class="formItem">
            		<label for="comment">Plants's features.</label>
        			<textarea placeholder="Comments" id="comment" name="comment" required></textarea>
        		</div>
        		<input type="submit" id="submit" value="Add" />
        	</form>
    	</div>
    	<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js'></script>
		<script src="resources/javascript/impress.js"></script>
	</body>
	</html>
	""")