class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        #self.income = my_dict(wage='wage', bonus='bonus')

class Position(Worker):
    def get_full_name(self):
        print(f'Имя сотрудника - {self.name} {self.surname}')

    def get_total_income(self, wage, bonus):
        value = wage + bonus
        print(f'Доход сотрудника составляет {value}')

worker_1 = Position('Andrey', 'Belov', 'manager')
worker_1.get_full_name()
worker_1.get_total_income(1258, 7852)

worker_2 = Position('Alex', 'Sidorov', 'supervisor')
worker_2.get_full_name()
worker_2.get_total_income(98541, 32058)