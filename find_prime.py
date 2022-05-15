from decimal_cal import *

def is_prime(x):
    i = "2"
    while True:
        if i == x:
            break
        if list_to_str(mod(x, i)) == "":
            # print("ang")
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
    i = add(i, "1")
