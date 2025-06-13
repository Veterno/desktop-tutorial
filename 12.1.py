class Apple:
    def __init__(self, w, c, s, t):
        self.weight=w
        self.color=c
        self.size=s
        self.taste=t
        print('Создано!')

Ap= Apple (10, 'красный', 5, 'сладкий')
print(Ap.weight)