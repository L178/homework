from sys import argv

name_script, hours_worked, hourly_rate, prize = argv

print('Количество отработаннх часов: ', hours_worked)
print('Ставка за час: ', hourly_rate)
print('Размер премии: ', prize)
arg_1 = int(hourly_rate)
arg_2 = int(hours_worked)
arg_3 = int(prize)
def wages (arg_1, arg_2, arg_3):
    return arg_1 * arg_2 + arg_3

print('Заработная плата составит: ', wages(arg_1, arg_2, arg_3))