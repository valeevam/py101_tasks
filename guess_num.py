"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""

if __name__ == '__main__':
    pass


import random
print('Hello! I have a secret in 0-1000000.Try to guess it! Or put - "stop".')
SECRET = round(random.random()*1000000)
low_b = 0
up_b = 1000000
try_num_no_stripped = input()
while True:
    mess=''
    try_num = try_num_no_stripped.strip()
    if try_num.isnumeric():
        if int(try_num) <= int(up_b) and int(try_num) >= int(low_b):
            if int(SECRET) == int(try_num):
                print('Wow! Great job! This is a SECRET %s' % (SECRET))
                break
            elif int(SECRET) > int(try_num):
                low_b = try_num
                mess = 'Secret is OVER ' + try_num +'. '
            else:
                up_b = try_num
                mess = 'Secret is UNDER ' + try_num +'. '
        else: 
            print('Number %s not in bounds - (%s, %s ).' % (try_num, low_b, up_b))
    elif try_num == 'stop':
        print('Oh... The SECRET is - ' + str(SECRET))
        break
    else:
        mess = try_num + ' - Is not number!'
    print('%sPut number in %s-%s or put "stop".' % (mess, low_b, up_b))
    try_num_no_stripped = input()
print('Good bye!')
