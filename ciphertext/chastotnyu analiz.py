import pprint

import random
__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-

alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"
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
pprint.pprint(dict)


for i in range(len(line)):
   if line[i] in alphabet:
       if str(line[i]) == 'ъ':
           line[i] = 'в'
       if str(line[i]) == 'л':
           line[i] = 'a'
       if str(line[i]) == 'й':
           line[i] = 'a'

print(line)
