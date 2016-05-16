'''
Created on 2011-12-02

@author: dnikolic
'''

empty_dict = {}
full_dict = {
    'WINDOWS': 'this is Windows!',
    'LINUX': 'this is Linux!',
    'MAC': 'this is MAC!'}

def get_dict_value(key, dict_):
    return dict_[key]

def check_dict(dict_, name):
    """Check if dictionary is empty"""
    if dict_:
        print '%s is not empty' % name
        print 'values are'
        for key, value in dict_.items():
            print 'key: %s; value: %s' % (key, value)
    else:
        print '%s is empty' % name
        
def check_if_key_exist(key, dict_):
    if key in dict_:
        print "1 Key '%s' exist! Value of this key is '%s'." % (key, dict_[key])
    else:
        print "1 Key '%s' does NOT exist!" % key

    if key not in dict_:
        print "N Key '%s' does NOT exist!" % key
    else:
        print "N Key '%s' exist! Value of this key is '%s'." % (key, dict_[key])

    try:
        print "E Key '%s' exist! Value of this key is '%s'." % (key, dict_[key])
    except KeyError:
        print "E Key '%s' does NOT exist!" % key
    finally:
        print 'This concludes key exist test.'
        
def set_default_for_key():
    dict_ = {}
    some_key = 'some_key'
    default_value = 'default_value' 
    value = dict_.get(some_key, default_value)
    print 'value for %s is %s' % (some_key, value)
 
def replace_key_in_dict(old_key, new_key, dict_):
    """
    Key is changed, but the value stays the same
    """
    print 'before replace: %s' % dict_
    dict_[new_key] = dict_.pop(old_key)
    print 'after replace: %s' % (dict_)

def delete_key(key1, key2, dict_):
    print 'before del: %s' % dict_
    del dict_[key1]
    print 'after del %s: %s' % (key1, dict_)
    v = dict_.pop(key2)
    print 'after pop %s: %s (v=%s)' % (key2, dict_, v)
    
def is_key_case_sensitive():
    test_dict = {
        'dragan': 'nikolic'}
    try:
        print 'Dragan - %s' % (test_dict['Dragan'])
    except Exception, e:
        print 'Keys ARE case sensitive - %s' % str(e)
        
def get_value_of_the_first_key():
    mydict = {'dragan': 'nikolic'}
    print 'value of first key is %s' % mydict.values()[0] 

def check_type():
    d = {}
    if type(d) is dict:
        print 'd is dict'
    else:
        print 'd is NOT dict'    
 
if __name__ == '__main__':
    #set_default_for_key()
    #check_type()
    #print get_dict_value('WINDOWS', full_dict)
    #print get_dict_value('LINUX', full_dict)
    #print get_dict_value('MAC', full_dict)
    
    #check_dict(empty_dict, 'empty_dict')
    #check_dict(full_dict, 'full_dict')
    
    #check_if_key_exist('ANDROID', full_dict)
    #check_if_key_exist('MAC', full_dict)

    #replace_key_in_dict('LINUX', 'UBUNTU', full_dict)
    #delete_key('MAC', 'WINDOWS', full_dict)
    #is_key_case_sensitive()
    get_value_of_the_first_key()
