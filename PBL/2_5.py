import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import time
import threading
import myfunc as my

def buzzer():
    print("ブザーon")
    time.sleep(10)
    print("ブザーoff")

#fromは高専ではst--d--@~じゃないとセキュリティ通らない
from_address = "pblgroup9.1@gmail.com"
password = "pbl123456"
to_address = "pblgroup9.2@gmail.com"
server = "smtp.gmail.com"
port = 587

switch = [0, 0, 0, 0, 0]#スイッチの状態を監視する変数、switch[0]は[1~n]の合計を示す
mailFlag = 0#深夜のうちにスイッチが開いたことを保存する変数
switchFlag = 0#スイッチが過去に開いたことがるかを保存する変数(wとaのどちらでファイルを開くかに使う)
refrigeOpening = 0#冷蔵庫が継続して開いていれば1

#現在の時刻を格納する変数
dt_now = datetime.datetime.now()
i=0
while i < 20:
    i = i + 1
    time.sleep(1)
    dt_now = datetime.datetime.now()
    print(dt_now.hour, "now 2-5")

    switch[1] = 1
    switch[0] = my.switchSum(switch)
    #print(switch[0], switch[1])

    if switch[0] == 0:
        refrigeOpening = 0 
    if switch[0] == 1:
        #スイッチが開いているときのif文
        mailFlag = 1
        if refrigeOpening == 0:
            refrigeOpening = 1
            switchFlag = my.report(switch, switchFlag)

            #ブザーを鳴らす関数を並列処理
            threadBuzzer = threading.Thread(target=my.buzzer)
            threadBuzzer.start()

if mailFlag == 1:
    print("mail in")
    mailFlag = 0
    my.mail(from_address, to_address, password, server, port)