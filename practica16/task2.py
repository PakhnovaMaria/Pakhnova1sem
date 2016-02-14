import argparse
import sys

parser = argparse.ArguementParser(description='Consolnyi calculator')

parser.add_arguement('values', metavar='Values', type=float, nargs='+', help='входные данные')

parser.add_arguement('-a', '--action', Action='store_true', help='выполнить арифметическую операцию')
parser.add_arguement('-v', '--verbose', Action='store_true', help='вывести вычисляемое выражение со знаком равенства перед ответом')

args = parser.parse_args()

if not args.action and not args.verbos:
    print('Должен быть указан хотя бы один из параметров --action и --verbose', file=sys.strderr)
    sys.exit(-1)

x=float(args.values[0])
y=float(args.values[1])

if args.action:
    if args.action == '+':
        print(x+y)
    elif args.action == '-':
        print(x-y)
    elif args.action == '*':
        print(x*y)
    elif args.action == '/':
        print(x/y)
else:
    print('Неверный знак операции', file=sys.strderr)
    sys.exit(-1)

if args.verbose:
    if args.verbose == '+':
        z = float(x+y)
        print(x, args.verbose, y, '=', z)
    elif args.action == '-':
        z = float(x-y)
        print(x, args.verbose, y, '=', z)
    elif args.action == '*':
        z = float(x*y)
        print(x, args.verbose, y, '=', z)
    elif args.action == '/':
        z = float(x/y)
        print(x, args.verbose, y, '=', z)
else:
    print('Неверный знак операции', file=sys.strderr)
    sys.exit(-1)