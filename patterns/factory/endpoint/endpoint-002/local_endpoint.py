"""
local_endpoint.py

Provides functions for managing a local PCoIP endpoint

Usage:
    import endpoint
    from local_endpoint import LocalEndpoint
    from remote_endpoint import RemoteEndpoint

    lep = LocalEndpoint(
                'tervdiwin7p9.teradici.com',
                {'username': 'teraauto', 'password': 'terapass', 'domain': 'teradici'},
                endpoint.VMW_VIEW_CLIENT,
                '5.1',
                'kvmoip',
                'core-kvmoip-1')
    lep = RemoteEndpoint(
                '192.168.0.10',
                {'username': 'teraauto', 'password': 'terapass', 'domain': 'teradici'},
                endpoint.VMW_VIEW_AGENT,
                '5.2',
                {'os_name': 'WINDOWS', 'os_version': '6.1', 'theme': 'classic'},
                'auto_w7p32h',
                'conn_server1.teradici.local')
    lep.connect_to_remote_endpoint(rep, endpoint.USER_INTERFACE, {'desktop_layout': 'windowLarge'})
    lep.disconnect_from_remote_endpoint(endpoint.DISCONNECT_AND_LOGOFF)
"""
from logger import TastLogger

from vmw_view_client import VmwViewClient
from tera1_client import Tera1Client

class ConnectionInterface:
    """
    Method to access a client
    """
    GUI = 'gui'  # access client via GUI (using e.g. Sikuli)
    API = 'api'  # access client via API (using e.g. CMICL, RPC)
    
class DisconnectionMethod:
    DISCONNECT = 'disconnect'
    DISCONNECT_AND_LOGOFF = 'disconnect_and_logoff'
   
class DesktopLayout:
    MULTIMONITOR = 'multimonitor'
    FULLSCREEN = 'fullscreen'
    WINDOW_SMALL = 'windowSmall'
    WINDOW_LARGE = 'windowLarge'
    WINDOW_SIZE = 'windowSize'

class LocalEndpointType:
    VMW_VIEW_CLIENT = 'vmw_view_client'
    TERA1_CLIENT = 'tera1_client'
    TERA2_CLIENT = 'tera2_client'
    TERADICI_WINDOWS_CLIENT = 'teradici_windows_client'
    ATLAS_CLIENT = 'atlas_client'

class LocalEndpoint(object):
    """
    LocalEndpoint class provides functions for managing local PCoIP endpoint.
    """

    def __init__(
        self, 
        fqdn, 
        username, 
        password,
        type, 
        version):
        """
        Arguments:
            fqdn: same as for Endpoint
            username: same as for Endpoint
            password: same as for Endpoint
            type: one of LocalEndpointType values
            version: same as for Endpoint
        """

        self.log = TastLogger(self.__class__.__name__)
        self.log.debug('LocalEndpoint: Creating new %s instance...' % self.__class__.__name__)
              
        if (type == LocalEndpointType.VMW_VIEW_CLIENT):
            self.local_endpoint = VmwViewClient(fqdn, username, password, version)

        elif (type == LocalEndpointType.TERA1_CLIENT):
            self.local_endpoint = Tera1Client(fqdn, username, password, version)

        else:
            self.log.error(
                'Unknown PCoIP client (%s)' % type)
            self.local_endpoint = None
            
        self.log.debug('LocalEndpoint: New %s instance created!' % self.__class__.__name__)

    def __getattr__(self, attr):
        """
        Invokes specified attribute implentation of the concrete class.
        """
        return getattr(self.local_endpoint, attr)
        

if __name__ == '__main__':
    lep = LocalEndpoint(
        'lep-fqdn001', 
        'teraauto', 
        'tera%%lab', 
        LocalEndpointType.VMW_VIEW_CLIENT,
        '1.2')
