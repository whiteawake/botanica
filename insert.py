#!/usr/bin/python
print 'Content-type: text/html\n\n'

import sqlite3, sys, cgi
import cgitb; cgitb.enable()

print("""
	<!DOCTYPE html>
	<html>
	<head>
		<title>Insert - Botanica</title>
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
			<h1 class='insetshadow' style="margin-left: -15px;">Insert New Data</h1>
			<div id="container">
			<div id="message" style="margin-left: -320px;">
					<a class="message" style=" margin-top: 10px; margin-left: 20px;" id="animate" href="home.py">Home</a>
				</div>
			</div>
    	</div>
    	<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js'></script>
		<script src="resources/javascript/impress.js"></script>
		<script src="resources/javascript/neotext_insert.js"></script>
	</body>
	</html>
	""")

plants_database = "plants.db"
locations_database = "locations.db"
families_database = "families.db"
#plants_file = "plants.txt"

pdb = sqlite3.connect(plants_database)
plant_cursor = pdb.cursor()
ldb = sqlite3.connect(locations_database)
location_cursor = ldb.cursor()
fdb = sqlite3.connect(families_database)
family_cursor = fdb.cursor()

records = plant_cursor.fetchall()
if (len(records) == 0):
	p = open('plants.txt', 'w')
	p.write(str("Jarrah" + ' | ' + "Eucalyptus marginata" +  ' | ' + "Perth" + ' | ' + "Myrtaceae" + ' | ' + "Long, stripey bark." + '\n'))
	p.write(str("Marri" + ' | ' + "Corymbia calophylla" +  ' | ' + "Mundaring" + ' | ' + "Myrtaceae" + ' | ' + "Thick trunks." + '\n'))
	p.write(str("Creeping Saltbush" + ' | ' + "Atriplex semibaccata" +  ' | ' + "Bunbury" + ' | ' + "Amaranthaceae" + ' | ' + "Round shape." + '\n'))
	p.write(str("Slender Devil's Twine" + ' | ' + "Cassytha glabella" +  ' | ' + "Kakadu" + ' | ' + "Lauraceae" + ' | ' + "Can display oval or elongated, pear shaped fruit." + '\n'))
	p.write(str("Black-anther Flax-lily" + ' | ' + "Dianella revoluta" +  ' | ' + "Mundaring" + ' | ' + "Xanthorrhoeaceae" + ' | ' + "First recorded in 1810 by Robert Brown." + '\n'))
	p.write(str("Silky Eremophila" + ' | ' + "Eremophila nivea" +  ' | ' + "King's Park" + ' | ' + "Scrophulariaceae" + ' | ' + "Critically endangered." + '\n'))
	p.write(str("Rottnest Island Daisy" + ' | ' + "Trachymene coerulea" +  ' | ' + "Rottnest Island" + ' | ' + "Araliaceae" + ' | ' + "Bright light blue flowers." + '\n'))
	p.write(str("Kurrajong" + ' | ' + "Brachychiton populneus" +  ' | ' + "Hobart" + ' | ' + "Malvaceae" + ' | ' + "Seeds are eaten by Aboriginal people after roasting." + '\n'))
	p.write(str("Palm Lily" + ' | ' + "Cordyline cannifolia" +  ' | ' + "Brisbane" + ' | ' + "Asparagaceae" + ' | ' + "Leaves vary from 20 to 50cm long." + '\n'))
	p.write(str("Milky Emu Bush" + ' | ' + "Eremophila lactea" +  ' | ' + "Kakadu" + ' | ' + "Scrophulariaceae" + ' | ' + "Critically endangered shrub producing a \"milky\" substance on it's leaves." + '\n'))
	p.write(str("Lake Varley Grevillea" + ' | ' + "Grevillea involucrata" +  ' | ' + "Varley" + ' | ' + "Proteaceae" + ' | ' + "Low-growing shrub, produces pink flowers" + '\n'))
	p.write(str("Corrigin grevillea" + ' | ' + "Grevillea scapigera" +  ' | ' + "Corrigin" + ' | ' + "Proteaceae" + ' | ' + "Small shrub endemic to the wheatbelt." + '\n'))
	p.write(str("Wild Rosemary" + ' | ' + "Olearia axillaris" +  ' | ' + "Rottnest Island" + ' | ' + "Asteraceae" + ' | ' + "Has very sharp leaves." + '\n'))
	p.write(str("Remote Thorny Lignum" + ' | ' + "Muehlenbeckia horrida" +  ' | ' + "California" + ' | ' + "Pinaceae" + ' | ' + "Extensively cultivated as a plantation timber." + '\n'))
	p.write(str("Western Underground Orchid" + ' | ' + "Rhizanthella gardneri" +  ' | ' + "Merredin" + ' | ' + "Orchidaceae" + ' | ' + "A small, critically endangered flower." + '\n'))
	p.write(str("Beach Spinifex" + ' | ' + "Spinifex longifolius" +  ' | ' + "Rottnest Island" + ' | ' + "Poaceae" + ' | ' + "Lives near beaches in coastal environments." + '\n'))
	p.write(str("Arum Lily" + ' | ' + "Zantedeschia aethiopica" +  ' | ' + "King's Park" + ' | ' + "Araceae" + ' | ' + "Displays white flowers from a clumping bulb." + '\n'))
	p.close()
	l = open('locations.txt', 'w')
	l.write(str("Perth" + ' | ' + "Sunny." +  '\n'))
	l.write(str("Mundaring" + ' | ' + "Cold and Raining." +  '\n'))
	l.write(str("Kakadu" + ' | ' + "Hot and Sunny." +  '\n'))
	l.write(str("King's Park" + ' | ' + "Sunny." +  '\n'))
	l.write(str("Rottnest Island" + ' | ' + "Cool Wind and Sunny." +  '\n'))
	l.write(str("Hobart" + ' | ' + "Stormy." +  '\n'))
	l.write(str("Brisbane" + ' | ' + "Cloudy." +  '\n'))
	l.write(str("California" + ' | ' + "Warm and Sunny." +  '\n'))
	l.write(str("Varley" + ' | ' + "Cloudy." +  '\n'))
	l.write(str("Merredin" + ' | ' + "Hot and Sunny." +  '\n'))
	l.write(str("Corrigin" + ' | ' + "Hot and Sunny." +  '\n'))
	l.close()
	f = open('families.txt', 'w')
	f.write(str("Myrtaceae" + '\n'))
	f.write(str("Xanthorrhoeaceae" + '\n'))
	f.write(str("Araliaceae" + '\n'))
	f.write(str("Scrophulariaceae" + '\n'))
	f.write(str("Lauraceae" + '\n'))
	f.write(str("Araceae" + '\n'))
	f.write(str("Poaceae" + '\n'))
	f.write(str("Amaranthaceae" + '\n'))
	f.write(str("Orchidaceae" + '\n'))
	f.write(str("Pinaceae" + '\n'))
	f.write(str("Asteraceae" + '\n'))
	f.write(str("Proteaceae" + '\n'))


	f.close()
else:
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Jarrah", "Eucalyptus marginata", "Perth", "Myrtaceae", "Long, stripey bark.")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Marri", "Corymbia calophylla", "Mundaring", "Myrtaceae", "Thick trunks.")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Creeping Saltbush", "Atriplex semibaccata", "Bunbury", "Amaranthaceae", "Round shape.")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Slender Devil's Twine", "Cassytha glabella", "Kakadu", "Lauraceae", "Can display oval or elongated, pear shaped fruit.")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Black-anther Flax-lily", "Dianella revoluta", "Mundaring", "Xanthorrhoeaceae", "First recorded in 1810 by Robert Brown.")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Silky Eremophila", "Eremophila nivea", "King's Park", "Scrophulariaceae", "Critically endangered.")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Rottnest Island Daisy", "Trachymene coerulea", "Rottnest Island", "Araliaceae", "Bright light blue flowers.")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Kurrajong", "Brachychiton populneus", "Hobart", "Malvaceae", "Seeds are eaten by Aboriginal people after roasting.")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Palm Lily", "Cordyline cannifolia", "Brisbane", "Asparagaceae", "Leaves vary from 20 to 50cm long.")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Milky Emu Bush", "Eremophila lactea", "Kakadu", "Scrophulariaceae", "Critically endangered shrub producing a \"milky\" substance on it's leaves.")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Lake Varley Grevillea","Grevillea involucrata", "Varley","Proteaceae","Low-growing shrub, produces pink flowers")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Corrigin grevillea", "Grevillea scapigera", "Corrigin", "Proteaceae", "Small shrub endemic to the wheatbelt.")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Wild Rosemary", "Olearia axillaris", "Rottnest Island", "Asteraceae", "Has very sharp leaves.")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Remote Thorny Lignum", "Muehlenbeckia horrida", "California", "Pinaceae", "Extensively cultivated as a plantation timber.")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Western Underground Orchid", "Rhizanthella gardneri", "Merredin", "Orchidaceae", "A small, critically endangered flower.)""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Beach Spinifex", "Spinifex longifolius", "Rottnest Island", "Poaceae", "Lives near beaches in coastal environments.")""")
	plant_cursor.execute("""INSERT INTO Plants (column_1, column_2, column_3, column_4, column_5) VALUES ("Arum Lily", "Zantedeschia aethiopica", "King's Park","Araceae","Displays white flowers from a clumping bulb.")""")

	location_cursor.execute("""INSERT INTO Locations (column_1, column_2) VALUES ("Perth", "Sunny.")""")
	location_cursor.execute("""INSERT INTO Locations (column_1, column_2) VALUES ("Mundaring", "Raining.")""")
	location_cursor.execute("""INSERT INTO Locations (column_1, column_2) VALUES ("Kakadu", "Moist.")""")
	location_cursor.execute("""INSERT INTO Locations (column_1, column_2) VALUES ("King's Park", "Cloudy")""")
	location_cursor.execute("""INSERT INTO Locations (column_1, column_2) VALUES ("Rottnest Island", "Sunny.")""")
	location_cursor.execute("""INSERT INTO Locations (column_1, column_2) VALUES ("Hobart", "Wet and Stormy.")""")
	location_cursor.execute("""INSERT INTO Locations (column_1, column_2) VALUES ("Brisbane", "Cloudy.")""")
	location_cursor.execute("""INSERT INTO Locations (column_1, column_2) VALUES ("California", "Warm and Sunny.")""")
	location_cursor.execute("""INSERT INTO Locations (column_1, column_2) VALUES ("Varley", "Cloudy.")""")
	location_cursor.execute("""INSERT INTO Locations (column_1, column_2) VALUES ("Merredin", "Hot and Sunny.")""")
	location_cursor.execute("""INSERT INTO Locations (column_1, column_2) VALUES ("Corrigin", "Hot and Sunny.")""")
	
	family_cursor.execute("""INSERT INTO Families (column_1) VALUES ("Myrtaceae")""")
	family_cursor.execute("""INSERT INTO Families (column_1) VALUES ("Xanthorrhoeaceae")""")
	family_cursor.execute("""INSERT INTO Families (column_1) VALUES ("Araliaceae")""")
	family_cursor.execute("""INSERT INTO Families (column_1) VALUES ("Scrophulariaceae")""")
	family_cursor.execute("""INSERT INTO Families (column_1) VALUES ("Lauraceae")""")
	family_cursor.execute("""INSERT INTO Families (column_1) VALUES ("Amaranthaceae")""")
	family_cursor.execute("""INSERT INTO Families (column_1) VALUES ("Poaceae")""")
	family_cursor.execute("""INSERT INTO Families (column_1) VALUES ("Araceae")""")
	family_cursor.execute("""INSERT INTO Families (column_1) VALUES ("Orchidaceae")""")
	family_cursor.execute("""INSERT INTO Families (column_1) VALUES ("Pinaceae")""")
	family_cursor.execute("""INSERT INTO Families (column_1) VALUES ("Asteraceae")""")
	family_cursor.execute("""INSERT INTO Families (column_1) VALUES ("Proteaceae")""")

	pdb.commit()
	ldb.commit()
	fdb.commit()
	plant_cursor.close()
	location_cursor.close()
	family_cursor.close()