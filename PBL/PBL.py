import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import time
import threading
import myfunc as my

#fromは高専では高専用アドレスじゃないとセキュリティ通らない
from_address = ""
password = ""
to_address = ""
#家:"smtp.gmail.com"
#高専:""
server = "smtp.gmail.com"
#家:587
#高専:
port = 587

switch = [0, 0, 0, 0, 0]#スイッチの状態を監視する変数、switch[0]は[1~n]の合計を示す
mailFlag = 0#深夜のうちにスイッチが開いたことを保存する変数
switchFlag = 0#スイッチが過去に開いたことがるかを保存する変数(wとaのどちらでファイルを開くかに使う)
refrigeOpening = 0#冷蔵庫が継続して開いていれば1

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

        switch[0] = my.switchSum(switch)

        if switch[0] == 0:
            refrigeOpening = 0 
        if switch[0] == 1:
            mailFlag =1
        #スイッチが開いているときのif文
            if refrigeOpening == 0:
                refrigeOpening = 1
                switchFlag = my.report(switch, switchFlag)

                #ブザーを鳴らす関数を並列処理
                threadBuzzer = threading.Thread(target=my.buzzer)
                threadBuzzer.start()

    
    if mailFlag == 1:
        mailFlag = 0
        my.mail(from_address, to_address, password, server, port)
    
            