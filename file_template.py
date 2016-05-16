'''
Created on 2012-07-23

@author: dnikolic
'''
import os

# define filename
filename = './file.cfg'

# template file has the same name as 'filename' with suffix '_template'
template_file = '%s_template%s' % os.path.splitext(filename)

# real values to be replaced in the template
template_values = {
    'name': 'Dragan',
    'address': 'Burnaby, BC'}

file_content = 'not defined!'

# read template file and replace template variables
try:
    fr = open(template_file, 'r')
    file_content = fr.read() % template_values
finally:
    fr.close()
    
# create real file
fw = open(filename, 'w')
try:
    fw.write(file_content)
finally:
    fw.close()
    

