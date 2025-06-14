import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Создаем объект класса Circle
circle = Circle(5)

# Вызываем метод area и выводим результат
print(circle.area())
