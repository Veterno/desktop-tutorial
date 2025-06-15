class Hexagon:
    def __init__(self, side):
        self.side = side
        

    def area(self):
        return side*6

# Создаем объект класса Hexagon с вводом основания и высоты
side = float(input("Введите длину стороны:"))

hexagon = Hexagon (side)

print (hexagon.area())
