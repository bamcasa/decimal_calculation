import numpy as np


def plus(num1, num2):
    if type(num2) == str:
        num2 = list(map(int, num2))
    if type(num1) == str:
        num1 = list(map(int, num1))
    li1 = num1
    li2 = num2

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
    return result


def minus(num1, num2):
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
    trans_arr = np.zeros(length, dtype=np.int8)

    for i in range(length):  # trans arr

        if i == 0 or i == length - 1:
            if arr2[i] == 0:
                trans_arr[i] = 0
            else:
                trans_arr[i] = 10 - arr2[i]
        else:
            trans_arr[i] = 9 - arr2[i]

    trans_arr = list(trans_arr)
    del(li1[0])
    del(trans_arr[0])
    result = plus(li1, trans_arr)
    result[0] = 0
    return result


num1 = "4628193"
num2 = "3198472"

result = minus(num1, num2)

print(result)
