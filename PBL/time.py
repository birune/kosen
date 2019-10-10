import time
import datetime

while 1:
    dt_now = datetime.datetime.now()
    while dt_now.hour < 2 or dt_now.hour > 5:
        time.sleep(1)
        dt_now = datetime.datetime.now()
        #print(dt_now.hour, "now not 2-5")
    
    if mailFlag == 1:
        

    while dt_now.hour >=2 and dt_now.hour <= 5:
        time.sleep(1)
        dt_now = datetime.datetime.now()
        #print(dt_now.hour, "now 2-5")
        if switch = 1: