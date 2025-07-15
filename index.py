#!/usr/bin/env python

print("Content-Type: text/html\n")

import sys, cgi
import cgitb; cgitb.enable()

print("""
	<!DOCTYPE html>
	<html>
		<head>
			<title>Botanica</title>
			<meta charset="UTF-8" />
			<meta name="author" content="Asha" />
			<link rel="icon" type="image/x-icon" href="resources/images/tree.png" />
			<link rel="stylesheet" type="text/css" href="resources/css/style.css" />
		</head>
		<body>
			<div class="log-form">
				<h2><img class="tree" src="resources/images/login_tree.png" />Botanica Login</h2>
				<form method="post" action="validation.py">
					<input type="text" id="username" name="username" placeholder="username" />
					<input type="password" id="password" name="password" placeholder="password" />
					<button type="submit" class="btn">Login</button>
					<a class="forgot" href="">Need an account?</a>
				</form>
  			</div>
		</body>
	</html>
	""")