import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import time
import threading

def buzzer():
    print("buzzer on")
    time.sleep(10)
    print("buzzer off")

def mail(from_address, to_address, password, server, port):
    f = open("mail.txt", "r")
    #messageにファイルの内容を入れる
    message = f.read()
    f.close

    msg = MIMEText(message)#本文
    msg["Subject"] = "refrigerator"#題
    msg["To"] = to_address#受信者
    msg["From"] = from_address#送信者
    msg["Date"] = formatdate()#日付

    #smtpサーバを指定してログイン
    smtpobj = smtplib.SMTP(server, port)
    smtpobj.ehlo()
        #高専で使用するときは
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(from_address, password)
        #ここまでコメントアウト
    
    #メールを送る
    smtpobj.sendmail(from_address, to_address, msg.as_string())
    smtpobj.close()

def report(switch, switchFlag):
    dt_now = datetime.datetime.now()
    opening = refrigeCheck(switch)

    if switchFlag == 0:
        f = open("mail.txt", "w")
        switchFlag = 1
    elif switchFlag == 1:
        f = open("mail.txt", "a")
                
    #ファイルへの書き込み
    f.write(str(dt_now.year) + "年")
    f.write(str(dt_now.month) + "月")
    f.write(str(dt_now.day) + "日")
    f.write(str(dt_now.hour) + "時")
    f.write(str(dt_now.minute) + "分")
    f.write(str(dt_now.second) + "秒に")
    f.write(str(opening))
    f.write("番の冷蔵庫開きました")

    f.close

    return switchFlag

def refrigeCheck(switch):
    for i in range(1, len(switch)):
        if switch[i] > 0:
            return i

def switchSum(switch):
    sum = 0
    for i in range(1, len(switch)):
        sum = sum + switch[i]
    
    return sum



    
