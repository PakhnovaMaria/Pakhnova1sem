from random import randint

O = open('float_data.txt', 'w')
for i in range(1000000):
    O.write(str(randint(0, 10000)/100)+' ')
O.close()
