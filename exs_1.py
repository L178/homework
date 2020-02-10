my_list = [12, 'Tom', 0.65, True, 789654, 'Moscow', 78.45]
el = len(my_list)
num_el = 0
while num_el <= el:
    print(f'{num_el} элемент списка - это ', type(my_list[num_el]))
    num_el += 1
