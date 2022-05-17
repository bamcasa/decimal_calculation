import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from decimal_cal import *

f = open("token.txt", 'r')
token = f.read()
print(token)
f.close()

def send_mail(title,text):
    global token
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('combeeh123@gmail.com', token)
    msg = MIMEText(text)
    msg['Subject'] = f"{title} {datetime.today().hour}시 {datetime.today().minute}분 {datetime.today().second}초"
    s.sendmail("combeeh123@gmail.com", "combeesang@gmail.com", msg.as_string())
    s.quit()


def is_mersenn_prime(p):
    num = power("2", p)
    num = subtract(num, "1")
    s = "4"
    i = "2"
    while True:
        if i == p:
            break
        s = mod(subtract(power(s, "2"), "2"), num)
        i = add(i, "1")
    s = list_to_str(s)
    return s == ""


i = "3"
while True:
    if i == "100":
        break
    print(f"n = {i}일때 시작","")
    send_mail(f"n = {i}일때 시작","")

    if is_mersenn_prime(i):
        num = power("2", i)
        num = subtract(num, "1")
        print(f"{num}, 2^{i}-1,n = {i}")
        send_mail("메르센소수 찾음",f"{num}, 2^{i}-1, n = {i}")

    i = add(i, "1")
