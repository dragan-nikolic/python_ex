'''
Created on 2011-08-09

@author: dnikolic
'''

import re

def find_pattern_in_string(pattern, string):
    '''Returns string that satisfies pattern if found
    Otherwise returns None 
    '''
    res = None
    
    try:
        res = re.compile(pattern).search(string).group()
    except:
        res = None    

    return res

def test_find_pattern_in_string():
    # Find exact 6 digits
    print '(1.1) ' + find_pattern_in_string('\d{6}', 'view_release_471234.zip') # 471234
    print '(1.2) ' + str(find_pattern_in_string('\d{6}', 'view_release_47123.zip')) # None

    # Find dot (.) followed by one or more characters at the end of the string
    print '(2.1) ' + find_pattern_in_string('\..+$', 'view_release_471234.gz') # .gz
    print '(2.2) ' + find_pattern_in_string('\..+$', 'view.release_471234.gz') # .release_471234.gz

    # Find dot (.) followed by one or more alphanumeric characters at the end of the string
    print '(3.1) ' + find_pattern_in_string('\.[\w]+$', 'view.release_471234.gz') # .gz
    print '(3.2) ' + find_pattern_in_string('\.\w+$', 'view.release_471234.gz') # .gz (same as previous)
    print '(3.3) ' + str(find_pattern_in_string('\.\w+$', 'view_release_471234_gz')) # None


def check_match(match, number_of_groups):
    nsafe = lambda x: match.group(x) if match.group(x) else "0"

    if match:
        return [nsafe(ix) for ix in range(number_of_groups+1)]
    else:
        return "INVALID"

def find_subgroups():
    # check time format [MM:]SS[,sss] (note that mins and millis are optional)
    # pattern: optional (1 or 2 digits followed by colon), followed by one or more digits, followed by optional (comma
    # followed by 1 to 3 digits)
    #pattern = "(\d{1,2}:)?\d+(,\d{1,3})?$"
    #number_of_groups = 2
    pattern = "((\d{1,2}):)?(\d+)(,(\d{1,3}))?$"
    number_of_groups = 5

    # can use either match or search, both OK
    value = "21:33,5"
    #match = re.match(pattern, value)
    match = re.search(pattern, value)
    print("{} is {}".format(value, check_match(match, number_of_groups)))

    # search is OK, match is INVALID
    value = ":33,5"
    #match = re.match(pattern, value)
    match = re.search(pattern, value)
    print("{} is {}".format(value, check_match(match, number_of_groups)))

    value = "1:33,"
    match = re.match(pattern, value)
    print("{} is {}".format(value, check_match(match, number_of_groups)))

    value = "1:33,5"
    match = re.match(pattern, value)
    print("{} is {}".format(value, check_match(match, number_of_groups)))

    value = "1:333,5"
    match = re.match(pattern, value)
    print("{} is {}".format(value, check_match(match, number_of_groups)))

    value = "919:33,5"
    match = re.match(pattern, value)
    print("{} is {}".format(value, check_match(match, number_of_groups)))



if __name__ == '__main__':
    #test_find_pattern_in_string()
    find_subgroups()