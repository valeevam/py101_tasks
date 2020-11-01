"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

if __name__ == '__main__':
    pass

import argparse
import os 
import nltk
from nltk.corpus import stopwords


def get_value (dict_pair):
    return dict_pair[1]

stop_words = stopwords.words("english") 
counting_words = {}
parser = argparse.ArgumentParser(description='Put filename to analyze it to top-100 frequency used words! \
                                (my_text.txt is default)')
parser.add_argument('filename', nargs='?', default = 'my_file.txt')
filename = parser.parse_args().filename

if os.path.isfile(filename) and os.path.getsize != 0 : 
    with open(filename, 'rt') as file_d : 
        for line in file_d:
            words = nltk.word_tokenize(line)
            words = [word for word in words if not word in stop_words and word.isalnum()]
            for word in words: 
                counting_words[word]=1 if word not in counting_words else counting_words[word]+1
    sorted_dict = sorted(counting_words.items(), key=get_value, reverse=True)
    top100 = 1
    print('Top 100 words in ' + filename + ':')
    for word in sorted_dict:
        if top100<=100 :
            print('%d. %s - %d entries' % (top100, word[0] , word [1]) ) 
        else: 
            break
        top100+=1                    
else: 
    print('You gave me something wrong.. %s is EMPTY or is NOT a file!' % (filename)) 

