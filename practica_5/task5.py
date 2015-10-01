from random import randint

O = open('int_data.txt', 'w')
for i in range(1000000):
    O.write(str(randint(0, 100))+' ')
O.close()