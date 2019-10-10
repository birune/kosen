from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib

from_address = ""
password = ""
to_address = ""

subject = "---test---"
f = open("mail.txt", "r")
message = f.read()
f.close
print(message)

msg = MIMEText(message)
msg["Subject"] = subject
msg["To"] = to_address
msg["From"] = from_address
msg["Date"] = formatdate()

smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.ehlo()
smtpobj.login(from_address, password)

smtpobj.sendmail(from_address, to_address, msg.as_string())
smtpobj.close()

