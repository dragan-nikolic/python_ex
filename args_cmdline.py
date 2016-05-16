import sys
import argparse

print 'All arguments from command line are: %s' % str(sys.argv)
print 'First argument is: %s' % sys.argv[1]
print 'All args starting with second are: %s' % str(sys.argv[2:])

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-m', action="store_true", dest='is_male', default=False)
parser.add_argument('-male', action="store_true", dest='is_male')
parser.add_argument('-t', action="store", dest='height', type=int, default=180, help="person's height")
parser.add_argument('-height', action="store", dest='height', type=int, help="person's height")
parser.add_argument('-n', action="store", dest="name", default='No Name') 
parser.add_argument('-name', action="store", dest="name") 

args = parser.parse_args()

print 'Arguments after processed by argparser are: %s' % str(args)

print 'Height is: %d' % args.height
