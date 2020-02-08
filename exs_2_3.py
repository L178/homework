month = int(input('Введите номер месяца: '))
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if month in winter:
    print('Это зима!')
elif month in spring:
    print('Это весна!')
elif month in summer:
    print('Это лето!')
elif month in autumn:
    print('Это осень!')
else:
    print('Вы ввели неверный номер месяца!')

