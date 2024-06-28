# to create email client session we import smtplib
import smtplib

# to create secure context we import ssl
import ssl

# to import environment variable
import os


def send_email(message):
	# default parameters required by smtp library
	host = "smtp.gmail.com"
	port = 465

	# it is recommended to use environment variables then below approach
	username = "wythsledonicdtrax@gmail.com"
	password = os.getenv("PASSWORD")

	# receiver user id
	receiver = "wythsledonicdtrax@gmail.com"

	# to create a secure context for sending emails securely - assign var
	context = ssl.create_default_context()

	# to test the code
	# message = """\
	# Subject: Portfolio_App Dev test
	# Test 1
	#Test 2
	#Test 3
	#"""

	with smtplib.SMTP_SSL(host, port, context=context) as server:
		server.login(username, password)
		server.sendmail(username, receiver, message)
