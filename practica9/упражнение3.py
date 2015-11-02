from decimal import *
#getcontext().prec = 2

Summa = int(input())
percent = float(input())
year = int(input())
def money(Summa,percent,year):
    P = percent/1200
    x = Summa * P * ((1 + P)**(year * 12))/ (-1 + (1 + P) ** (year * 12))
    return x
def overpay(Summa, percent, year):
    over = money(Summa, percent, year) * 12 * year - Summa
    return over
#from Decimal import Decimal, getcontext
print(((Decimal(money(Summa, percent, year)).quantize(Decimal('0.01'))),Decimal(overpay(Summa, percent, year)).quantize(Decimal('0.01'))))
