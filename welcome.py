#!/usr/bin/env python

print "Content-Type: text/html\n"

import sqlite3, sys, cgi, csv
import cgitb; cgitb.enable()

print("""
	<!DOCTYPE html>
	<html>
		<head>
			<meta http-equiv="refresh" content="15;url=home.py">
			<meta charset='UTF-8'>	
			<title>Welcome - Botanica</title>
			<meta name="author" content="Asha" />
			<link rel="icon" href="resources/images/tree.png" type="image/x-icon">
			<link rel='stylesheet' href='resources/css/letters.css'>
			<embed src="resources/audio/rescue_neville.mp3" autostart="true" hidden="true">
			<style>
				html { 
					background: black; 
				}
				@font-face {
					font-family: nyala;
					src: url('../resources/nyala.ttf');
					src: local(nyala), url(''../resources/nyala.ttf')    
					format('opentype');
				}
				html, body { 
					overflow: hidden; 
				}
				#poster { 
					width: 890px; 
					margin: 30px auto; 
	  				font-family: nyala;
 				}
 				#poster h1 {
		 			color: mediumaquamarine; 
 					background: url(resources/images/garden.jpg) 20px -150px no-repeat;
					font-size: 180px;
					line-height: 0.7;
					text-align: center; 
					-webkit-background-clip: text;
					-webkit-text-fill-color: transparent;
					letter-spacing: -8px; 
					-webkit-transition: all 6.5s; 
					padding-bottom: 40px; 
				}
 				.step-one #poster h1 {
		 			padding-top: 220px; 
 				}
				#poster h1 span { 
					-webkit-transition: all 6.5s;
					-moz-transition: all 6.5s;
					-o-transition: all 6.5s;
				}
				#poster h1 span.char1 { margin-left: -1450px; } 
				#poster h1 span.char2 { margin-left: 200px; }
				#poster h1 span.char3 { margin-left: 200px; }
				#poster h1 span.char5 { margin-left: 1450px; }
				#poster h1 span.char6 { margin-left: 200px; }
				#poster h1 span.char7 { margin-left: 200px; }
				#poster h1 span.char8 { margin-left: 200px; }
				#poster h1 span.char9 { margin-left: 200px; }
				.step-one #poster h1 span { margin: 0; }
		 		
 				#poster p { text-align: center; font-size: 30px; letter-spacing: 20px; }
 				#poster p span { position: relative; -webkit-transition: all 6.5s ease; color: white; }
 				.step-two #poster p span { top: 0 !important; left: 0 !important; }
			</style>
			<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'></script>
			<script src="resources/javascript/jquery.lettering.js"></script>
			<script>
				$(function() {
					$("#poster h1, #poster p").lettering();
					$("#poster p span").each(function() {  $(this).css({ top: -(Math.floor(Math.random()*1001)+1500), left: Math.floor(Math.random()*1001)-500,  }); });
					setTimeout(function() {$('html').addClass("step-one");}, 2000);
					setTimeout(function() {$('html').addClass("step-two");}, 4000);
				});
			</script>
		</head>
			<h2><a style="position: fixed; top: 7px; right: 7px; color: white; text-decoration: none;" href="botanica.py" title="Skip introduction">Skip</a></h2>
			<script type='text/javascript' src='resources/javascript/jquery.easing.1.2.js'></script>
			<script type='text/javascript' src='resources/javascript/jquery.circulate.js'></script>
	       	<script type='text/javascript' src='resources/javascript/example.js'></script>
		<body>
		<div id="poster">
			<h1>Botanica</h1>
			<p>The Plant Database.</p>
		</div>	
		</body>
	</html>
	""")