from random2 import randint

N = int(input("Введите размер массива: "))
a = []
for i in range(N):
    a.append(randint(1, 9999))
a.sort()
print(a)

value = int(input("Введите число для поиска в массиве: "))

mid = len(a) // 2
low = 0
high = len(a) - 1

while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
else:
    print("ID =", mid)