"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

	
if __name__ == '__main__':
    pass

passwd = input('Put password\n')

found_al = False
found_num = False
for c in passwd: 
    found_al = c.isalpha() 
    if found_al: break
for c in passwd: 
    found_num = c.isnumeric() 
    if found_num: break

print('good!') if found_num and found_al and len(passwd) >= 8 else print('not good :((')