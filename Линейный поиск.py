from random2 import randint

b = 1

N = int(input("Введите размер массива: "))
a = []
for i in range(N):
	a.append(randint(1, 9999))
a.sort()
print (a)

key = int(input("Введите искомое число: "))

for i in range(len(a)):
	if a[i] == key:
		b = 2
		print ("ID = ", str(i))

if b != 2: 
	print("No value")