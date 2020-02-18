my_list = [8, 36, 9, 78, 8, 19, 25, 9, 78, 11, 3]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)