from email.mime.text import MIMEText
from email.utils import formatdate

from_address = "PBLgroup9.1"
password = "pbl123456"
to_address = "PBLgroup9.2"

msg = MIMEText("test")
msg['Subject'] = "subject"
msg['From'] = from_address
msg['To'] = to_address
msg['Date'] = formatdate()