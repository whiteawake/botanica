#!/usr/bin/env python

print("Content-Type: text/html\n")

import cgi, sys
import cgitb; cgitb.enable()

form = cgi.FieldStorage()


password = form.getvalue('password')
username = form.getvalue('username')

if ((username == 'dbudd') and (password == 'Plant7')):
	print("<meta http-equiv=\"refresh\" content=\"0; url=/botanica/login/dbudd/\">")
elif ((username == 'nsouth') and (password == 'Plant8')):
	print("<meta http-equiv=\"refresh\" content=\"0; url=/botanica/login/nsouth/\">")
elif ((username == 'asha') and (password == 'Plant9')):
	print("<meta http-equiv=\"refresh\" content=\"0; url=/botanica/login/asha/\">")
elif ((username == 'dblayn') and (password == 'Plant10')):
	print("<meta http-equiv=\"refresh\" content=\"0; url=/botanica/login/dblayn/\">")
else:
	print("<script type=\"text/javascript\">window.alert(\"Incorrect username/password!\");</script>"),
	print("<meta http-equiv=\"refresh\" content=\"0; url=/botanica/\">")