from configobj import ConfigObj

    
root = ConfigObj('test_plan.ini')

print type(root), root

for item in root:
    print type(item), item
    print type(root[item]), root[item]

for platform in ['platform1', 'platform2', 'platform3']:    
    print type(root['PLATFORMS'][platform]['local_ep']), root['PLATFORMS'][platform]['local_ep']
    
    if type(root['PLATFORMS'][platform]['local_ep']) is str:
        print 'STRING: %s' % root['PLATFORMS'][platform]['local_ep']
        root['PLATFORMS'][platform]['local_ep'] = [root['PLATFORMS'][platform]['local_ep']]
        print 'converted to list: ', type(root['PLATFORMS'][platform]['local_ep']), root['PLATFORMS'][platform]['local_ep']
        
    elif type(root['PLATFORMS'][platform]['local_ep']) is list:
        print 'LIST'
    else:
        print 'Ooops'

