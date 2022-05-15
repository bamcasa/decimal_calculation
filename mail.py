import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from decimal_cal import *

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login('combeeh123@gmail.com', 'rcmdnfjognwfdcgs')

def is_prime(x):
    i = "2"
    while True:
        if i == x:
            break
        if list_to_str(mod(x, i)) == "":
            return False

        i = add(i, "1")
    return True

i = "2"
while True:
    if i == "100":
        break
    num = power("2", i)
    num = subtract(num, "1")
    if is_prime(num):
        print(f"{num}, 2^{i}-1")
        msg = MIMEText(f"{num}, 2^{i}-1")
        msg['Subject'] = f"메르센소수 찾음 {datetime.today().hour}시 {datetime.today().minute}분 {datetime.today().second}초"
        s.sendmail("combeeh123@gmail.com", "combeesang@gmail.com", msg.as_string())

    i = add(i, "1")


