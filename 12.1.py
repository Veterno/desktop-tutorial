class Apple:
    def __init__(self, weight, color, size, taste):
        self.w=weight
        self.c=color
        self.s=size
        self.t=taste
        print('Создано!')

Ap = Apple (10, 'красный', 5, 'сладкий')
print(Ap.weight)