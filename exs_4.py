my_string = input('Введите слова через пробел: ')
my_list = my_string.split()
for el in my_list:
    print(f'{my_list.index(el) + 1} - {el[:10]}')