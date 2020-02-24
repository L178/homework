class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')

pen_1 = Pen('num1')
pen_1.draw()
pencil_1 = Pencil('num2')
pencil_1.draw()
handle_1 = Handle('num3')
handle_1.draw()

