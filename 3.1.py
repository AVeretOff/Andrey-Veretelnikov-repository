from SecondLab import SecondLab
from table import header_table, line_for_table

dx = input("dx=")
r = input("r=")
try:
    dx = float(dx)
    r = float(r)
except ValueError:
    print("Введите число.")
    exit()
header_table()
x0 = -10
x1 = 8

while x0 <= x1:
    y = SecondLab(r, x0)
    print("{:<1} {:<20} {:<1} {:<20} {:<1}".format('|', round(x0, len(str(dx))), "|", y.func(), '|'))
    line_for_table()
    x0 += dx