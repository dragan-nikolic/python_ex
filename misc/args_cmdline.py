"""
Great tutorial: https://realpython.com/command-line-interfaces-python-argparse/
"""

import sys
import argparse

print('All arguments from command line are: %s' % str(sys.argv))
if len(sys.argv) > 1:
    print('First argument is: %s' % sys.argv[1])
if len(sys.argv) > 2:
    print('All args starting with second are: %s' % str(sys.argv[2:]))

def parse_args():
    parser = argparse.ArgumentParser(description='Short sample app')

    parser.add_argument('filename', nargs='+', help='file names') # can specify multiple, must specify at least one
    parser.add_argument('--date_column', action="store", default='load_dttm') # optional argument with defauly value
    parser.add_argument('--date_filter', action="store") # optional argument, no default value, can be None
    parser.add_argument("--size", choices=["S", "M", "L", "XL"], default="M") # provides choices with default value
    parser.add_argument('-m', action="store_true", dest='is_male', default=False, help="short for --male")
    parser.add_argument('--male', action="store_true", dest='is_male', help="set if male")
    parser.add_argument('-t', action="store", dest='height', type=int, default=180, help="short for --height")
    parser.add_argument('--height', action="store", dest='height', type=int, help="person's height")
    parser.add_argument('--name', action="append", dest="name") # can specify multiple times

    return parser.parse_args()

args = parse_args()

print('Arguments after processed by argparser are: %s' % str(args))

print('table_spec is: %s' % args.table_spec)
print(f'name: {args.name}')
