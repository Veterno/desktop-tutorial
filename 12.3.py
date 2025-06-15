class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Создаем объект класса Triangle с вводом основания и высоты
base = float(input("Введите основание треугольника: "))
height = float(input("Введите высоту треугольника: "))
triangle = Triangle(base, height)

# Вызываем метод area и выводим результат
print("Площадь треугольника:", triangle.area())
