I = open('input.txt')
O = open('output.txt', 'w')
C = tuple(int(i) for i in I.readline().split())
line, column = C
temp = [[float(x) for x in I.readline().split()] for i in range (line)]
for j in range(column):
    min = temp[0][j]
    for i in range(line):
        if temp[i][j] < min:
            min = temp[i][j]
    O.write(str(min))
O.close()






