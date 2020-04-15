import math

class SecondLab:
    def __init__(self, radius=0, x=0, y=0):
        self.r = radius
        self.x = x
        self.y = y

    def func(self):
        if self.x >= -10 and self.x < -8:
            return -3
        elif self.x >= -8 and self.x < -3:
            return self.x + 3
        elif self.x >= -3 and self.x < 3:
            return -(math.sqrt(self.r ** 2 - self.x ** 2))
        elif self.x >= 3 and self.x < 5:
            return self.x - 3
        elif self.x >= 5 and self.x <= 8:
            return 3
        else:
            return None

    def __shot(self):
        k = (0 + self.r) / (0 - (self.r / 2))
        b = -self.r - k * (self.r / 2)
        # и сделаем тоже самое для второй прямой
        k1 = (-self.r) / (self.r / 2)
        b1 = -self.r - k * 0
        if self.y > 0 and self.y < math.sqrt(self.r ** 2 - self.x ** 2):
            return True
        if self.y > k * self.x + b and self.y > k1 * self.x + b1 and self.y < 0:
            return True
        else:
            return False

    def message(self):
        if self.__shot():
            return "Попадание."
        else:
            return "Промах."
