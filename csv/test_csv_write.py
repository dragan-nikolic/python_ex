import csv
import sys

f = open(sys.argv[1], 'wt')
try:
    writer = csv.writer(f, dialect='excel-tab')
    writer.writerow( ('Title 1', 'Title 2', 'Title 3') )
    for i in range(10):
        writer.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)) )
finally:
    f.close()

print open(sys.argv[1], 'rt').read()