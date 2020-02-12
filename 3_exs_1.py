num_1 = float(input('Введите любое число: '))
num_2 = float(input('Введите любое число: '))
if num_2 != 0:
    my_func = lambda arg_1, arg_2: arg_1 / arg_2
    print(my_func(num_1, num_2))
else:
    print('Делить на ноль нельзя!')
