import smtplib

from_address = "PBLgroup9.1"
password = "pbl123456"
to_address = "PBLgroup9.2"

smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.ehlo()
smtpobj.login(from_address, password)