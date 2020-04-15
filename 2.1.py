import SecondLab
# r это радиус окружности


r = input("r=")
x = input("x=")
try:
    r = float(r)
    x = float(x)
except ValueError:
    print("R и x должны быть числами.")
#если x лежит за пределами диапозона значений, то выведем исключение собственное
if x < -10 or x > 8:
    raise ValueError("Неподходящее значение.")
    exit()
y = SecondLab.SecondLab(r, x)
print("y=", y.func())
