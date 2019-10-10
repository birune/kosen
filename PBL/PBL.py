import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

from_address = ""
password = ""
to_address = ""

switch = 0
mailFlag = 0
switchFlag = 0

sendfile = open("mail.txt", "w")
dt_now = datetime.datetime.now()

while 1:
    while dt_now.hour < 2 or dt_now.hour > 5:
        time.sleep(1)
        dt_now = datetime.datetime.now()
        #print(dt_now.hour, "now not 2-5")

    while dt_now.hour >=2 and dt_now.hour <= 5:
        time.sleep(1)
        dt_now = datetime.datetime.now()
        #print(dt_now.hour, "now 2-5")
        if switch = 1:
            mailFlag = 1
            if switchFlag == 0:
                f = open("mail.txt", "w")
                switchFlag = 1
            elif switchFlag == 1:
                f = open("mail.txt", "a")
            
            f.write(str(dt_now.year) + "年")
            f.write(str(dt_now.month) + "月")
            f.write(str(dt_now.day) + "日")
            f.write(str(dt_now.hour) + "時")
            f.write(str(dt_now.minute) + "分")
            f.write(str(dt_now.second) + "秒に冷蔵庫が開きました。\n")
    
    if mailFlag == 1:
        f = open("mail.txt", "r")
        message = f.read()
        f.close

        msg = MIMEText(message, charset)
        msg["Subject"] = "refrigerator"
        msg["To"] = to_address
        msg["From"] = from_address
        msg["Date"] = formatdate()


            