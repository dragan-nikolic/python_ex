import csv
import sys

f = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(f, dialect='excel-tab')
    fieldnames = reader.next()
    print 'fieldnames are: %s' % fieldnames
    for row in reader:
        print row
        
    print 'number of rows: %s' % reader.line_num
finally:
    f.close()
    
