"""
remote_endpoint.py
"""

from logger import TastLogger

from vmw_win7_view_host import VmwWin7ViewHost
from vmw_winxp_view_host import VmwWinXpViewHost


class RemoteEndpointType:
    VMW_WIN7_VIEW_HOST = 'vmw_win7_view_host'
    VMW_WINXP_VIEW_HOST = 'vmw_winxp_view_host'
    TERA1_WIN7_HOST = 'tera1_win7_host'
    TERA2_WINXP_HOST = 'tera2_winxp_host'
    
class RemoteEndpoint(object):
    """
    RemoteEndpoint class provides remote endpoint specific functionality
    """

    def __init__(
        self,
        fqdn,
        username, 
        password,
        type,
        version,
        os_info,
        vm_name,
        connection_server):
        """
        Arguments:
            fqdn: same as for Endpoint
            username: same as for Endpoint
            password: same as for Endpoint
            type: same as for Endpoint
            version: same as for Endpoint
            os_info: {'os_name', 'os_version', 'os_theme', 'system_type'}
            vm_name:
            connection_server:
        """
        self.log = TastLogger(self.__class__.__name__)
        self.log.debug('RemoteEndpoint: Creating new %s instance...' % (
                                    self.__class__.__name__))
                                    
        if (type == RemoteEndpointType.VMW_WIN7_VIEW_HOST):
            self.rep = VmwWin7ViewHost(fqdn, username, password, version, os_info, vm_name, connection_server)

        elif (type == RemoteEndpointType.VMW_WINXP_VIEW_HOST):
            self.rep = VmwWinXpViewHost(fqdn, username, password, version, os_info, vm_name, connection_server)

        else:
            self.log.error(
                'Unknown PCoIP host (%s)' % type)
            self.rep = None
            
        self.log.debug('RemoteEndpoint: New %s instance created!' % self.__class__.__name__)
        
    def __getattr__(self, attr):
        """
        Invokes specified attribute implentation of the concrete class.
        """
        return getattr(self.rep, attr)
        
