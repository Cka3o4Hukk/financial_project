first_dep = int(input('Введите число без пробелов: \n'))
percent = int(input('Введите процент начисления: \n'))  # 14
month = int(input('Введите количество месяцев: \n'))  # 3


year_profit = first_dep * percent * 0.01  
profit_on_month = year_profit / 12 
final_amount = first_dep * ((1+percent/1200)**month)  # итог 1035


print(f'\nЧистый плюс в первый месяц: {(profit_on_month)} рублей')
print(f'Баланс в конце 1 месяца: {(first_dep + profit_on_month)} рублей')
print(f'Баланс в конце срока: {(final_amount)} sss')


'''
1000

1011
1022

'''
