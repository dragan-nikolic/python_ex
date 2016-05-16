import argparse

from configobj import ConfigObj

parser = argparse.ArgumentParser(description='Testplan app')

parser.add_argument('-p', action="store", dest='testplan_file')

args = parser.parse_args(['-p', 'testplan.ini'])
#args = parser.parse_args(['-p', 'platforms.ini'])
print args

testsets = {}
platforms = {}
testlists = {}
endpoints = {}

def process_include(include_section):
    if type(include_section) is list:
        return include_section
    
    include_section = include_section.split(',')
    
    include_list = []
    for item in include_section:
        include_list.append(item.strip())
        
    return include_list
    
def process_testsets(section):
    for key in section:
        testsets[key] = section[key]
 
def process_testlists(section):
    for key in section:
        testlists[key] = section[key]
 
def process_platforms(section):
    for key in section:
        platforms[key] = section[key]
 
def process_endpoints(section):
    for key in section:
        endpoints[key] = section[key]
 
def read_testplan_file(tpfile):
    file_content = ConfigObj(tpfile)

    # process INCLUDE section  
    if 'INCLUDE' in file_content:  
        include_list = process_include(file_content['INCLUDE'])
        for item in include_list:
            read_testplan_file(item)
    
    # process TESTSETS section
    if 'TESTSETS' in file_content:  
        process_testsets(file_content['TESTSETS'])
    
    # process TESTLISTS section
    if 'TESTLISTS' in file_content:  
        process_testlists(file_content['TESTLISTS'])
    
    # process PLATFORMS section
    if 'PLATFORMS' in file_content:  
        process_platforms(file_content['PLATFORMS'])
    
    # process ENDPOINTS section
    if 'ENDPOINTS' in file_content:  
        process_endpoints(file_content['ENDPOINTS'])
    
    
read_testplan_file(args.testplan_file)

print testsets
print testlists
print platforms
print endpoints
