#!/usr/bin/env python

print "Content-Type: text/html\n"

import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

location = form.getvalue('location')
weather = form.getvalue('weather')

f = open('locations.txt', 'a')
f.write(str(location + ' | ' + weather + '\n'))
f.close()
print("""
	<!DOCTYPE html>
	<html>
	<head>
		<title>Add - Botanica</title>
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
		<h2 class="descript"> 
		Location successfully added to database:</h2><font color="white"><p><br />"""
		+ 'Location: ' + location + '<br />' + 'Weather comments: ' + weather +
		"""
		</p></font>
		</div>
    	<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js'></script>
		<script src="resources/javascript/impress.js"></script>
	</body>
	</html>
	"""),
print('<meta http-equiv="refresh" content="5; url=/botanica/by_location.py">')