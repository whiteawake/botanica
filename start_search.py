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
	<title>Starting - Botanica</title>
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

start_letter = form.getvalue('start_letter')
values = { "start_letter": start_letter + '%' }

print("<h2 class='descript' style='margin-left: -8%;'>Common name starting with '" + start_letter + "'</h2>")

plant_cursor.execute("""SELECT COUNT(column_1) FROM Plants
			    WHERE column_1 LIKE :start_letter""", values)

records = plant_cursor.fetchall()

if(len(records) == 0):
    print('<font color="white">There are no plants with a common name starting with ' + start_letter + '</font>')
else:
    print('<font color="white">There are ' + str(records[0][0]) + ' plants with a name starting with \'' + start_letter + '\'</font>')
print('<br /><br />')

plant_cursor.execute('''SELECT column_1, column_2, column_4, column_3
		    FROM Plants
		    WHERE column_1 LIKE :start_letter''', values)
fields = ["Common name", "Scientific name", "Family", "Location"]
records = plant_cursor.fetchall()
print_Records(records, fields)

#print('This next query is hard coded')
#print("<h2 class='descript' style='margin-left: 0%;'>Plants who's common name ends with 'ae'</h2>")

#plant_cursor.execute('''SELECT COUNT(column_1) FROM Plants
			    #WHERE column_1 LIKE "%ae"''')

#records = plant_cursor.fetchall()

#if(len(records) == 0):
    #print("There are no plants with a common name ending with 'ae'")
#else:
    #print 'There are ' + str(records[0][0]) + " plants with a name ending with 'ae'"
#print '<br /><br />'

#plant_cursor.execute('''SELECT column_3, column_1, column_2
#		    FROM Plants
#		    WHERE column_1 LIKE "%ae"''')
#fields = ["Location", "Common name", "Scientific name"]
#records = plant_cursor.fetchall()
#print_Records(records, fields)


pdb.commit()
plant_cursor.close()
print("""
	</div>
	<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js'></script>	
	</body></html>
	""")