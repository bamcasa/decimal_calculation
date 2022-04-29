import numpy as np

num1 = "99999"
num2 = "99999"

li1 = list(map(int, num1))
li2 = list(map(int, num2))

if len(li1) >= len(li2):
    length = len(li1)
else:
    length = len(li2)

li1.insert(0, 0)
li2.insert(0, 0)

arr1 = np.array(li1)
arr2 = np.array(li2)

if len(arr1) >= len(arr2):
    length = len(arr1)
else:
    length = len(arr2)

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

print(result)
