class Road:
    def __init__(self, lenght, width):
        self.param_1 = lenght
        self.param_2 = width

    def weight(self):
        value = self.param_1*self.param_2*25*5
        print(f'Масса асфальта на данную дорогу: {value}')


r_1 = Road(15, 65)
r_1.weight()
