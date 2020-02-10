my_list = [8, 6, 4, 4, 2, 2]
new_el = int(input('Введите число: '))
for el in my_list:
    
pos = my_list.index(el)
my_list.isert(pos, new_el)
print(my_list)