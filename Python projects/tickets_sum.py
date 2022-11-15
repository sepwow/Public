#Задание 13.8.19

sum = 0
tickets_n = int(input("Введите кол-во билетов: \n"))
for i in range(tickets_n):
    i += 1
    if i < tickets_n + 1:
        age = int(input(f'Возраст гостя для билета № {i}: '))
        if 0 < age < 18:
            i += 1
            print('Билет бесплатный')
        elif 18 <= age <= 25:
            i +=1
            sum += 990
            print('Стоимость билета: 990 руб')
        else:
            i += 1
            sum += 1390
            print('Стоимость билета: 1390 руб.')
if tickets_n > 3:
    sum = sum - ((sum / 100) * 10)
    print(f'Сумма {sum} руб. с учётом скидки 10%')
else:
    print(f'Сумма {sum} руб. без скидки')