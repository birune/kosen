import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

from_address = ""
password = ""
to_address = ""

switch = 0#スイッチの状態を監視する変数
mailFlag = 0#深夜のうちにスイッチが開いたことを保存する変数
switchFlag = 0#スイッチが過去に開いたことがるかを保存する変数(wとaのどちらでファイルを開くかに使う)

#smtpサーバにログインしたりなんだりする
smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.ehlo()
smtpobj.login(from_address, password)

#現在の時刻を格納する変数
dt_now = datetime.datetime.now()

while 1:
    #1~2, 5~24時の間のループ
    while dt_now.hour < 2 or dt_now.hour > 5:
        time.sleep(1)
        dt_now = datetime.datetime.now()
        #print(dt_now.hour, "now not 2-5")

    #2~5時のループ
    while dt_now.hour >=2 and dt_now.hour <= 5:
        time.sleep(1)
        dt_now = datetime.datetime.now()

        #print(dt_now.hour, "now 2-5")
        #スイッチが開いているときのif文
        if switch == 1:
            mailFlag = 1
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
            f.write(str(dt_now.second) + "秒に冷蔵庫が開きました。\n")

            #ここら辺にブザーを鳴らす処理
            #time.sleepの時間によってなる時間が変化する

    
    if mailFlag == 1:
        f = open("mail.txt", "r")
        #messageにファイルの内容を入れる
        message = f.read()
        f.close

        msg = MIMEText(message)#本文
        msg["Subject"] = "refrigerator"#題
        msg["To"] = to_address#受信者
        msg["From"] = from_address#送信者
        msg["Date"] = formatdate()#日付

        #smtpサーバにログインしたりなんだりする
        smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(from_address, password)
        
        #メールを送る
        smtpobj.sendmail(from_address, to_address, msg.as_string())
        smtpobj.close()

            