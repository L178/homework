num_1 = float(input('Введите число: '))
num_2 = float(input('Введите число: '))
num_3 = float(input('Введите число: '))
def my_sum(var_1, var_2, var_3):
    min_1 = min(num_1, num_2, num_3)
    return var_1 + var_2 + var_3 - min_1

print(my_sum(num_1, num_2, num_3))