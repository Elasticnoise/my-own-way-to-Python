# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
# user_input = input("Введите, пожалуйста, номер месяца: ")
# month = int(user_input)
# print('Вы ввели', month)

year = {1: '31 день', 2: '29 дней', 3: '31 день', 4: '30 дней',
        5: '31 день', 6: '30 дней', 7: '31 день', 8: '31 день',
        9: '30 дней', 10: '31 день', 11: '30 дней', 12: '31 день'}
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

if int(user_input) <= 12:
    print('В этом месяце', year[month])
else:
    print('Вы не знаете сколько месяцев в году? Введите от 1 - 12!')

# зачет!
