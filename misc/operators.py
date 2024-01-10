"""
Created on 2012-02-12

@author: dnikolic
"""


def use_logical_operators(os_name='WINDOWS', os_version='5.1'):
    if os_name == 'WINDOWS' and os_version == '5.1':
        print 'OS is WinXP!'
    else:
        print 'OS is not XP'

    if ((os_name == 'WINDOWS') and 
        (os_version == '5.1')):
        print 'Told you, WinXP!'
    else:
        print 'Told you, not XP!'


def use_arithmetic_operators():
    x = 5
    print 'x=%d' % x
    
    x += 9
    print 'x=%d' % x
         
    x /= 2
    print 'x=%d' % x


if __name__ == '__main__':
    use_logical_operators()
    use_logical_operators('LINUX')
    #use_arithmetic_operators()
    pass
