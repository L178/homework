sec = int(input('Введите количество секунд: '))
hour = sec // 3600
sec_1 = sec - (hour * 3600)
min = sec_1 // 60
sec_2 = sec_1 - (min * 60)
print(f'чч: {hour} мм: {min} сс: {sec_2}')

