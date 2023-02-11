# Домашнее задание после Урока 30
# Создайте класс на тему животных. В классе должен присутствовать конструктор не менее трёх методов.
class Animals:
    def __init__(self, type, area, size):
        self.type = type
        self.area = area
        self.size = size
    def first(self):
        print('\nВид животного: ' + self.type)
    def second(self):
        print('Место обитания: ' + self.area)
    def third(self):
        print('Популяция: ' + str(self.size) + ' особей.')

opisanie1 = Animals ('Кошка', 'везде, кроме крайнего Севера и Юга', 175468324)
opisanie1.first()
opisanie1.second()
opisanie1.third()

#  В класс из предыдущего урока добавьте три класса-наследника на ваше усмотрение.
class Fly(Animals):
    def __init__(self, type, area, size):
        super().__init__(type, area, size)
    def fly(self):
        print('Это летающая птица.\n')
class Water(Animals):
    def __init__(self, type, area, size):
        super().__init__(type, area, size)
    def water(self):
        print('Это водоплаващая птица.\n')

class NoFly(Animals):
    def __init__(self, type, area, size):
        super().__init__(type, area, size)
    def nofly(self):
        print('Это нелетающая птица.')

bird1 = Fly('Утка', 'Европа', 321354)
bird1.first()
bird1.second()
bird1.third()
bird1.fly()
bird2 = Water('Лебедь','Евразия', 1544135)
bird2.first()
bird2.second()
bird2.third()
bird2.water()
bird3 = NoFly('Страус', 'Африка', 3213215)
bird3.first()
bird3.second()
bird3.third()
bird3.nofly()