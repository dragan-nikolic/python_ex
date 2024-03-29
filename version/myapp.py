import argparse

parser = argparse.ArgumentParser(description='My App')

parser.add_argument('myarg', help='my mandatory argument')
parser.add_argument('--version', action='version', version='%(prog)s 1.1.0')

args = parser.parse_args()

print('Arguments after processed by argparser are: %s' % str(args))
