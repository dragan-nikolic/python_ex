"""
Created on 2012-12-19

@author: dnikolic

Note: This module was originali named string.py.
That caused AttributeError in args_cmdline.py example (and in general would cause 
problem in any module importing string :(
That's why it is renamed to string_ex.py :)
"""

string1 = "red fox"
string2 = "Red Fox"


def compare_strings_case_sensitive(str1, str2):
    if str1 == str2:
        print "Strings '%s' and '%s' are case sensitive equal" % (str1, str2)
    else:
        print "Strings '%s' and '%s' are NOT case sensitive equal" % (str1, str2)


def compare_strings_case_insensitive(str1, str2):
    if str1.lower() == str2.lower():
        print "Strings '%s' and '%s' are case insensitive equal" % (str1, str2)
    else:
        print "Strings '%s' and '%s' are NOT case insensitive equal" % (str1, str2)


def split_string(string_to_split, delimiter):
    part1, rest = string_to_split, None
    if delimiter in string_to_split:
        print 'delimiter found'
        part1, rest = string_to_split.split(delimiter)
    else:
        print 'no delimiter found'
    print part1
    print rest


def string_parts():
    mystring = "dragan"

    print "len({}) = {}".format(mystring, len(mystring))
    print "{}[0] = {}".format(mystring, mystring[0])
    print "{}[:0] = {}".format(mystring, mystring[:0])
    print "{}[:1] = {}".format(mystring, mystring[:1])
    print "{}[0:1] = {}".format(mystring, mystring[0:1])
    print "{}[:2] = {}".format(mystring, mystring[:2])
    print "{}[0:2] = {}".format(mystring, mystring[0:2])
    print "{}[:4] = {}".format(mystring, mystring[:4])
    print "{}[0:4] = {}".format(mystring, mystring[0:4])
    print "{}[0:len] = {}".format(mystring, mystring[0:len(mystring)])
    print "{}[1:] = {}".format(mystring, mystring[1:])
    print "{}[:-1] = {}".format(mystring, mystring[:-1])
    print "{}[:-2] = {}".format(mystring, mystring[:-2])
    mystring = mystring[0] + "l" + mystring[2:]
    print mystring


def write_char_at_position(string, position, char):
    if position == 0:
        string = char + string[1:]
    elif position >= len(string)-1:
        string = string[:position] + char
    else:
        string = string[:position] + char + string[position+1:]
    return string


def test_write_char_at_position():
    print write_char_at_position("dragan", 1, "l")

if __name__ == '__main__':
    # compare_strings_case_sensitive(string1, string2)
    # compare_strings_case_insensitive(string1, string2)
    # split_string('teradici\\dragan', '\\')
    # split_string('dragan', '\\')
    string_parts()
    #test_write_char_at_position()