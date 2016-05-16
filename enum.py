'''
Created on 2012-11-29

@author: dnikolic
'''

def enum(**enums):
    return type('Enum', (), enums)

class LocalEndpointType:
    VIEW_CLIENT = 'view_client'
    ZERO_CLIENT = 'zero_client'
    
RemoteEndpointType = enum(
    VIEW_HOST = 'view_host',
    TERA1_HOST = 'tera1_host')
    

if __name__ == '__main__':
    print 'LEP VIEW_CLIENT = %s' % LocalEndpointType.VIEW_CLIENT
    print 'REP VIEW_HOST = %s' % RemoteEndpointType.VIEW_HOST