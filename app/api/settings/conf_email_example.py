"""
config email
change this file, first change name file conf_email_example.py to conf_email.py
"""
EMAILUSETLS = False
EMAILUSESSL = True
EMAILHOST = "your.host.com"
EMAILPORT = 465
EMAILHOSTUSER = "your_user@host.com"
EMAILHOSTPASSWORD = "your_password"
EMAILBACKEND = "django_smtp_ssl.SSLEmailBackend"
DEFAULTFROMEMAIL = "your@email_ref.com"
URLPRODUCTION = "http://127.0.0.1:8000"
