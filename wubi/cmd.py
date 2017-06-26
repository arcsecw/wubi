import argparse
from wubi import get

from _compat import u


def wubi():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", help="chinese2wubi:cw,wubi2chinese wc")
    parser.add_argument("-c", help="Input chinese words")
    args = parser.parse_args()

    if args.t not in ['wc','cw']:
        parser.print_help()
        return
    if not args.c:
        parser.print_help()
        return
    print(get(u(args.c),args.t))

if __name__ == '__main__':
    wubi()