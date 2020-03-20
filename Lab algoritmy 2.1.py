import math as m
flag = 1
while flag ==1:
    x = float(input("Введите x "))
    if (x >= -10 and x < -8):
        y = -3
    elif (x >= -8 and x < -3):
        y = x * 0.6 + 1.77
    elif (x >= -3 and x < 3):
        y = 0 + m.sqrt((x - 0)**2 - 3**2)
    elif (x >= 3 and x < 5):
        y = x - 3
    elif (x >= 5):
        y = 3
    print ("Значение парамера y = " + str(y))
