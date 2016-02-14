import argparse
import sys

parser = argparse.ArgumentParser(description='Consolnyi calculator')

parser.add_argument('values', metavar='Values', type=float, nargs='+', help='Dannie')
parser.add_argument('-a', '--action', action="store", help='vupolnit operaziu')

parser.add_argument('-v', '--verbose', action="store", help='vuvesti vuragenie')

args = parser.parse_args()

if not args.action and not args.verbose:
    print('ukazan odin iz parametrov --action i --verbose', file=sys.stderr)
    sys.exit(-1)

x=float(args.values[0])
y=float(args.values[1])

if args.action:
    if args.action == '+' or '-' or '*' or '/':
        if args.action == '+':
            print(x+y)
        elif args.action == '-':
            print(x-y)
        elif args.action == '*':
            print(x*y)
        elif args.action == '/':
            print(x/y)
    else:
        print('nevernui znak operazii', file=sys.stderr)
        sys.exit(-1)

if args.verbose:
    if args.action == '+' or '-' or '*' or '/':
        if args.verbose == '+':
            z = x+y
            print(x, args.verbose, y, '=', z)
        elif args.verbose == '-':
            z = x-y
            print(x, args.verbose, y, '=', z)
        elif args.verbose == '*':
            z = x*y
            print(x, args.verbose, y, '=', z)
        elif args.verbose == '/':
            z = x/y
            print(x, args.verbose, y, '=', z)
    else:
        print('nevernui znak operazii', file=sys.stderr)
        sys.exit(-1)
