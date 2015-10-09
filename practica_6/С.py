I=open('input.txt')
amount = int(I.readline())
slippers = [float(x) for x in I.readline().split()]
c = amount
for i in range(amount):
    for j in range(i+1, amount):
        if slippers[j] == (-1) * slippers[i]:
            if slippers[j] > 0:
                c = min(c, j-i)
O=open('output.txt','w')
O.write(str(c))
O.close()

