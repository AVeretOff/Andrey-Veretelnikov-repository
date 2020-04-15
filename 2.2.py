from SecondLab import SecondLab

r = input("r=")
x = input("x=")
y = input("y=")
try:
    r = float(r)
    x = float(x)
    y = float(y)
except ValueError:
    print("Вводите пожалуйста числа")
    exit()
msg = SecondLab(r, x, y)
print(msg.message())