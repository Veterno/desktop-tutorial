#Конструктор обьекта
class Apple:
    def __init__(self, name, color, weight, price):
        self.name=name
        self.color=color
        self.weight=weight
        self.price=price

#Создание свойств обьекта
name=str(input(''))
color=str(input('')) 
weight=int(input(''))
price=int(input(''))

#Создание самого обьекта и передача его в переменную 
apple = Apple(name, color, weight, price)

#Показ обьекта на экране 
print (apple.name)  