I = open('input.txt')
bargain = int(I.readline())
coins = [int(x) for x in I.readline().split()]
amount = 0
fives = 0
for coin in coins:
    if coin == 5:
        fives += 1
    else:
        change = (coin - 5)//5
        if fives > 0:
            if fives >= change:
                fives -= change
            else:
                amount += change - fives
                fives = 0
        else:
            amount += change
O=open('output.txt','w')
O.write(str(amount))
O.close()


