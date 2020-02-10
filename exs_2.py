my_list = input('Введите все, что хотите: ')
print(list(my_list))
el = len(my_list)
print(el)
def my_new_list(s):
    symbols = list(my_list)
    for el in range(len(my_list) // 2):
        tmp = symbols[el]
        symbols[el] = symbols[el + 1]
        symbols[el + 1] = tmp
    return ''.join(symbols)
data = my_new_list(my_list)
print(data)