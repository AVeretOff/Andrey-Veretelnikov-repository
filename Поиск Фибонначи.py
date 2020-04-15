from bisect import bisect_left
from random2 import randint

def fibMonaccianSearch(arr, x, n):

    fibMMm2 = 0 # (м-2) -ый номер Фибоначчи
    fibMMm1 = 1 # (м-1) 'й Фибоначчи №
    fibM = fibMMm2 + fibMMm1 # m'th Фибоначчи
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
    offset = -1;
    while (fibM > 1):
        i = min(offset+fibMMm2, n-1)
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else :
            return i
    if(fibMMm1 and arr[offset+1] == x):
        return offset+1;
    return -1

n = int(input("Введите размер массива: "))
arr = []

for i in range(n):
    arr.append(randint(1, 9999))
arr.sort()
print(arr)

x = int(input("Введите искомое число: "))

print("Found at index:", fibMonaccianSearch(arr, x, n))

