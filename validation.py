#!/usr/bin/env python

print("Content-Type: text/html\n")

import cgi, sys
import cgitb; cgitb.enable()

form = cgi.FieldStorage()


password = form.getvalue('password')
username = form.getvalue('username')

if ((username == 'dbudd') and (password == 'Plant7')):
	print("<meta http-equiv=\"refresh\" content=\"0; url=/botanica/login/dbudd/\">")
elif ((username == 'asha') and (password == 'Plant7')):
	print("<meta http-equiv=\"refresh\" content=\"0; url=/botanica/login/asha/\">")
elif ((username == 'dblayn') and (password == 'Plant7')):
	print("<meta http-equiv=\"refresh\" content=\"0; url=/botanica/login/dblayney/\">")
else:
	print("<script type=\"text/javascript\">window.alert(\"Incorrect username/password!\");</script>"),
	print("<meta http-equiv=\"refresh\" content=\"0; url=/botanica/\">")