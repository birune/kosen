
import datetime
dt_now = datetime.datetime.now()

f = open("mail.txt", "w")
f.write("hello\n")
f.close

f = open("mail.txt", "a")

f.write(str(dt_now.year) + "年")
f.write(str(dt_now.month) + "月")
f.write(str(dt_now.day) + "日")
f.write(str(dt_now.hour) + "時")
f.write(str(dt_now.minute) + "分")
f.write(str(dt_now.second) + "秒に冷蔵庫が開きました\n")

f.write("goodbye\n")
f.close

f = open("mail.txt", "r")
message = f.read()
f.close
print(message)