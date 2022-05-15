import numpy as np


def list_to_str(result):
    result = ' '.join(map(str, result)).replace(" ", "")
    result = result.lstrip('0')
    return result


def trans_complement(arr, length):
    arr = list(map(int, arr))
    for i in range(length - len(arr)):
        arr.insert(0, 0)

    for i in range(length):
        arr[i] = 9 - arr[i]
    arr = list_to_str(arr)
    arr = add(arr, "1")
    return arr


def add(num1, num2):
    li2 = list(map(int, num2))
    li1 = list(map(int, num1))

    if len(li1) >= len(li2):
        length = len(li1) + 1
        for i in range(length - len(li2)):
            li2.insert(0, 0)
        li1.insert(0, 0)
    else:
        length = len(li2) + 1
        for i in range(length - len(li1)):
            li1.insert(0, 0)
        li2.insert(0, 0)

    arr1 = np.array(li1)
    arr2 = np.array(li2)
    # print(arr1)
    # print(arr2)
    arr3 = np.zeros(length, dtype=np.int8)

    result = np.zeros(length, dtype=np.int8)

    arr1 = np.flip(arr1)
    arr2 = np.flip(arr2)

    for i in range(length):
        sum = arr1[i] + arr2[i] + arr3[i]
        if sum >= 10:
            arr3[i + 1] += 1
            result[i] = sum % 10
        else:
            result[i] += sum

    result = np.flip(result)
    # print(result)
    result = list_to_str(result)
    return result


def subtract(num1, num2):
    li2 = list(map(int, num2))
    li1 = list(map(int, num1))
    if len(li1) >= len(li2):
        length = len(li1)
    else:
        length = len(li2)

    arr1 = np.array(li1)
    arr2 = np.array(li2)
    trans_arr = trans_complement(arr2, length)
    # print(num1 ,trans_arr)
    result = add(num1, trans_arr)
    # print(length)
    # print(len(result))
    # print(len(li1),len(li2))
    #
    # print("변환X " + result)
    # print("변환O " + trans_complement(result, length))
    if length == len(result) - 1:  # 양수
        result = result[-length:]
        # print("양수")
    elif length >= len(result):  # 음수
        result = "-" + trans_complement(result, length)
        # print("음수")

    return result


def multiply(num1, num2):
    sum = "0"
    for i in range(int(num2)):
        sum = add(sum, num1)
    return sum

def divide(num1,num2):
    i = "0"
    while True:
        num1 = subtract(num1,num2)
        if num1[0] == "-":
            break
        i = add(i,"1")
    return i
def mod(num1,num2):
    while True:
        n = subtract(num1,num2)
        if n[0] == "-":
            break
        num1 = n
    return num1

num1 = "123"
num2 = "11"

result = mod(num1, num2)
# result = list_to_str(result)
print(result)
