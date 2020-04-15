import math
from table import header_table, line_for_table

def teilor(x, n):
    sum = 0
    for i in range(n):
        sum += ((-1) ** i * x ** i) / math.factorial(i)
    return sum

dx = input("dx=")
x0 = input("x0=")
x1 = input("x=")
n = input("n=")
try:
    dx = float(dx)
    x0 = float(x0)
    x1 = float(x1)
    n = int(n)
except ValueError:
    print("Извините введите число.")
    exit()
header_table()
while x0 <= x1:
    y = teilor(x0, n)
    line_for_table()
    print("{:<1} {:<20} {:<1} {:<20} {:<1}".format('|', round(x0, len(str(dx))), "|", round(y, len(str(n))), '|'))
    line_for_table()
    x0 += dx
