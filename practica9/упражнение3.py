from decimal import *
# getcontext().prec = 2


def money(summa, percent, year):
    p = percent/1200
    x = summa * p * ((1 + p)**(year * 12)) / (-1 + (1 + p) ** (year * 12))
    return x


def overpay(summa, percent, year):
    over = money(summa, percent, year) * 12 * year - summa
    return over

# from Decimal import Decimal, getcontext

summa = int(input())
percent = float(input())
year = int(input())

value1 = Decimal(money(summa, percent, year)).quantize(Decimal('0.01'))
value2 = Decimal(overpay(summa, percent, year)).quantize(Decimal('0.01'))

print(value1, value2)
