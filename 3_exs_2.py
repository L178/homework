name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birth_year = input('Введите год рождения: ')
place = input('Введите город проживания: ')
email = input('Введите email: ')
telephon = input('Введите телефон: ')
def my_func(var_1, var_2, var_3, var_4, var_5, var_6):
    print(f'Имя - {var_1}, Фамилия - {var_2}, Год рождения - {var_3}, Город проживания - {var_4}, email - {var_5}, телефон - {var_6}')
my_func(var_1=name, var_2=surname, var_3=birth_year, var_4=place, var_5=email, var_6=telephon)