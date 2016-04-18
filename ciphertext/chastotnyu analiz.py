import pprint

import random
__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
signs = ' .,-“”()1234567890XVIABCDEFGHIJKLMNOPQRSTUWVXYZabcdifjhigklmnopqrstuvwxyz’'
class Monoalphabet:

    def __init__(self, keytable):
        lowercase_code = {self.alphabet[i]:keytable[i] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():keytable[i].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode = {}  # FIXME

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        for letter in line:
            if letter in alphabet:
                if letter == 'ъ':
                    letter = 'в'
                if letter == 'л':
                    letter = 'a'
        return line


line = input()
count = 0
graph = {}
for letter in line:
    if letter in alphabet:
        if letter not in graph:
            graph[letter] = 1
        else:
            graph[letter] += 1
    count += 1
A = []
for letter in graph:
    b = (int((graph[letter]/count)*10000)/100)
    graph[letter] = b
    A.append(graph[letter])
dict = {}
for letter in graph:
    dict[graph[letter]] = letter
#print(graph)
#pprint.pprint(dict)

print(len(line))
i = 0
for letter in line:
    if letter in alphabet:
        if str(letter) == 'ъ':
            line = line[0:i] + 'в' + line[i+1:]
        if str(letter) == 'ч':
            line = line[0:i] + 'a' + line[i+1:]
        if str(letter) == 'й':
            line = line[0:i] + 'и' + line[i+1:]
        if str(letter) == 'ы':
            line = line[0:i] + 'т' + line[i+1:]
        if str(letter) == 'ш':
            line = line[0:i] + 'к' + line[i+1:]
        if str(letter) == 'с':
            line = line[0:i] + 'д' + line[i+1:]
        if str(letter) == 'о':
            line = line[0:i] + 'л' + line[i+1:]
        if str(letter) == 'д':
            line = line[0:i] + 'е' + line[i+1:]
        if str(letter) == 'л':
            line = line[0:i] + 'о' + line[i+1:]
        if str(letter) == 'н':
            line = line[0:i] + 'б' + line[i+1:]
        if str(letter) == 'ю':
            line = line[0:i] + 'с' + line[i+1:]
        if str(letter) == 'х':
            line = line[0:i] + 'у' + line[i+1:]
        if str(letter) == 'в':
            line = line[0:i] + 'р' + line[i+1:]
        if str(letter) == 'ь':
            line = line[0:i] + 'з' + line[i+1:]
        if str(letter) == 'ё':
            line = line[0:i] + 'я' + line[i+1:]
        if str(letter) == 'я':
            line = line[0:i] + 'ь' + line[i+1:]
        if str(letter) == 'а':
            line = line[0:i] + 'н' + line[i+1:]
        if str(letter) == 'и':
            line = line[0:i] + 'п' + line[i+1:]
        if str(letter) == 'у':
            line = line[0:i] + 'ю' + line[i+1:]
        if str(letter) == 'е':
            line = line[0:i] + 'ж' + line[i+1:]
        if str(letter) == 'э':
            line = line[0:i] + 'й' + line[i+1:]
        if str(letter) == 'ф':
            line = line[0:i] + 'х' + line[i+1:]
        if str(letter) == 'п':
            line = line[0:i] + 'ч' + line[i+1:]
        if str(letter) == 'р':
            line = line[0:i] + 'ф' + line[i+1:]
        if str(letter) == 'з':
            line = line[0:i] + 'м' + line[i+1:]
        if str(letter) == 'ц':
            line = line[0:i] + 'ы' + line[i+1:]
        if str(letter) == 'ж':
            line = line[0:i] + 'ш' + line[i+1:]
        if str(letter) == 'к':
            line = line[0:i] + 'э' + line[i+1:]
        if str(letter) == 'м':
            line = line[0:i] + 'ё' + line[i+1:]
        if str(letter) == 'б':
            line = line[0:i] + 'ц' + line[i+1:]


        if str(letter) == 'Ъ':
            line = line[0:i] + 'В' + line[i+1:]
        if str(letter) == 'Ч':
            line = line[0:i] + 'А' + line[i+1:]
        if str(letter) == 'Й':
            line = line[0:i] + 'И' + line[i+1:]
        if str(letter) == 'Ы':
            line = line[0:i] + 'Т' + line[i+1:]
        if str(letter) == 'Ш':
            line = line[0:i] + 'К' + line[i+1:]
        if str(letter) == 'С':
            line = line[0:i] + 'Д' + line[i+1:]
        if str(letter) == 'О':
            line = line[0:i] + 'Л' + line[i+1:]
        if str(letter) == 'Д':
            line = line[0:i] + 'Е' + line[i+1:]
        if str(letter) == 'Л':
            line = line[0:i] + 'О' + line[i+1:]
        if str(letter) == 'Н':
            line = line[0:i] + 'Б' + line[i+1:]
        if str(letter) == 'Ю':
            line = line[0:i] + 'С' + line[i+1:]
        if str(letter) == 'Х':
            line = line[0:i] + 'У' + line[i+1:]
        if str(letter) == 'В':
            line = line[0:i] + 'Р' + line[i+1:]
        if str(letter) == 'Ь':
            line = line[0:i] + 'З' + line[i+1:]
        if str(letter) == 'Ё':
            line = line[0:i] + 'Я' + line[i+1:]
        if str(letter) == 'Я':
            line = line[0:i] + 'Ь' + line[i+1:]
        if str(letter) == 'А':
            line = line[0:i] + 'Н' + line[i+1:]
        if str(letter) == 'И':
            line = line[0:i] + 'П' + line[i+1:]
        if str(letter) == 'У':
            line = line[0:i] + 'Ю' + line[i+1:]
        if str(letter) == 'Е':
            line = line[0:i] + 'Ж' + line[i+1:]
        if str(letter) == 'Э':
            line = line[0:i] + 'Й' + line[i+1:]
        if str(letter) == 'Ф':
            line = line[0:i] + 'Х' + line[i+1:]
        if str(letter) == 'П':
            line = line[0:i] + 'Ч' + line[i+1:]
        if str(letter) == 'Р':
            line = line[0:i] + 'Ф' + line[i+1:]
        if str(letter) == 'З':
            line = line[0:i] + 'М' + line[i+1:]
        if str(letter) == 'Ц':
            line = line[0:i] + 'Ы' + line[i+1:]
        if str(letter) == 'Ж':
            line = line[0:i] + 'Ш' + line[i+1:]
        if str(letter) == 'К':
            line = line[0:i] + 'Э' + line[i+1:]
        if str(letter) == 'М':
            line = line[0:i] + 'Ё' + line[i+1:]
        if str(letter) == 'Б':
            line = line[0:i] + 'Ц' + line[i+1:]
        i += 1
    if letter in signs:
        i += 1
print(line)

