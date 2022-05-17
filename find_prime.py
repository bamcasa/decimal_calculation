from decimal_cal import *

def is_mersenn_prime(p):
    num = power("2", p)
    num = subtract(num, "1")
    s = "4"
    i = "2"
    while True:
        if i == p:
            break
        s = mod(subtract(power(s,"2"),"2"),num)
        i = add(i,"1")
    s = list_to_str(s)
    return s == ""

i = "3"
while True:
    # if i == "6":
    #     break
    if is_mersenn_prime(i):
        num = power("2", i)
        num = subtract(num, "1")
        print(f"{num}, 2^{i}-1, n = {i}")
    i = add(i, "1")
