'''
Created on 2012-11-29

@author: dnikolic
'''

from enum import Enum


def enum(**enums):
    return type('Enum', (), enums)

class LocalEndpointType:
    VIEW_CLIENT = 'view_client'
    ZERO_CLIENT = 'zero_client'
    
RemoteEndpointType = enum(
    VIEW_HOST = 'view_host',
    TERA1_HOST = 'tera1_host')

class StorageSystem(Enum):
    LOCALFS = "localfs"
    ADLS = "adls"
    SMB = "smb"
    SFTP = "sftp"
    

if __name__ == '__main__':
    print('LEP VIEW_CLIENT = %s' % LocalEndpointType.VIEW_CLIENT)
    print('REP VIEW_HOST = %s' % RemoteEndpointType.VIEW_HOST)

    print(f'StorageSystem.LOCALFS: {StorageSystem.LOCALFS}')
    print(f'StorageSystem.LOCALFS.name: {StorageSystem.LOCALFS.name}')
    print(f'StorageSystem.LOCALFS.value: {StorageSystem.LOCALFS.value}')

    print()

    print(f'type(StorageSystem.LOCALFS): {type(StorageSystem.LOCALFS)}')
    print(f'type(StorageSystem.LOCALFS.name): {type(StorageSystem.LOCALFS.name)}')
    print(f'type(StorageSystem.LOCALFS.value): {type(StorageSystem.LOCALFS.value)}')
