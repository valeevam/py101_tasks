"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное



def exists_even_num (*given_nums):
    for num in given_nums: 
        if num % 2 == 0: 
            return True 
    return False


# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."


def sell_alcohol ():
    print ('your bottle, please')


age = 17
sell_alcohol() if age >= 21 else print ('Мы не продаём алкоголь несовершеннолетним.')


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()


def is_python_keyword(str_to_check):
    import keyword
    return keyword.iskeyword(str_to_check)


# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."

def get_type_rus (obj_to_check):
    rus_types = {
        type('') : 'Это срока',
        type(1) : 'Это целое число',
        type(1.1) : 'Это вещественное число', 
        type([1,2,3]) : 'Это список',
        type({1:1, 2:2}) : 'Это словарь'
    }
    type_of_obj=type(obj_to_check)
    print(rus_types[type_of_obj]) if type_of_obj in rus_types else print('Не могу перевести, Тип переменной '+ str(type_of_obj))

