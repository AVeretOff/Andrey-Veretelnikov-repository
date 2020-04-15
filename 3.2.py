from SecondLab import SecondLab
for i in range(10):
    r = input("r=")
    x = input("x=")
    y = input("y=")
    try:
        r = float(r)
        x = float(x)
        y = float(y)
    except ValueError:
        print("Вводите пожалуйста числа")
    msg = SecondLab(r, x, y)
    print(msg.message())