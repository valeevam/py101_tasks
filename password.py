"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

if __name__ == '__main__':
    pass


passwd = input('Put password\n')
print('good!') if passwd.isalnum and len(passwd) >= 8 else print('not good :((')