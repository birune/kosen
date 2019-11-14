import time
import threading

def buzzer():
    print("ブザーon")
    time.sleep(10)
    print("ブザーoff")

def write():
    print("ファイルに書き込み")
    time.sleep(5)

threadBuzzer = threading.Thread(target=buzzer)
threadBuzzer.start()
print("start")
time.sleep(7)
print("5 seconds")
time.sleep(7)
print("end")