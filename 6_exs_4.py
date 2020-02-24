class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        print('Машина повернула направо')

    def show_speed(self):
        print(f'Вы едете со скоростью {speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Вы превысили скорость!')
        else:
            print(f'Вы едете со скоростью {self.speed} км/ч')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость!')
        else:
            print(f'Вы едете со скоростью {self.speed} км/ч')

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

car_1 = TownCar(15, 'red', 'Mazda', False)
car_1.show_speed()
car_2 = WorkCar(41, 'green', 'Lexus', True)
car_2.show_speed()



