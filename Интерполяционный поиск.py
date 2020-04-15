from random2 import randint

def interpolation_search(array, key):
    minimum = 0
    maximum = len(array) - 1
    ret = 0
    while array[minimum] < key < array[maximum]:
        mid = int(minimum + (maximum - minimum) * (key - array[minimum]) / (array[maximum] - array[minimum]))
        if array[mid] == key:
            ret = mid
            break
        elif array[mid] > key:
            maximum = mid - 1
        else:
            minimum = mid + 1

    if array[minimum] == key:
        ret = minimum
    if array[maximum] == key:
        ret = maximum
    while ret > 0 and array[ret - 1] == key:
        ret -= 1
    if array[ret] == key:
        return 'ID = ' + str(ret)
    else:
        return "No value"


N = int(input("Введите размер массива: "))
array = []
for i in range(N):
    array.append(randint(1, 9999))
array.sort()
print(array)

key = int(input("Введите искомое число: "))

print(interpolation_search(array, key))