"""
remote_endpoint_base.py

abstract class that defines RemoteEndpoint interface
"""

from logger import TastLogger

from endpoint_base import EndpointBase


class RemoteEndpointBase(EndpointBase):
    """
    RemoteEndpoint class provides remote endpoint specific functionality
    """

    def __init__(
        self,
        fqdn,
        username, 
        password,
        version,
        os_info,
        vm_name,
        connection_server):
        """
        Arguments:
            fqdn: same as for Endpoint
            username: same as for Endpoint
            password: same as for Endpoint
            version: same as for Endpoint
            os_info: {'os_name', 'os_version', 'os_theme', 'system_type'}
            vm_name:
            connection_server:
        """
        self.log = TastLogger(self.__class__.__name__)
        self.log.debug('RemoteEndpointBase: Creating new %s instance...' % (
                                    self.__class__.__name__))
        
        super(RemoteEndpointBase, self).__init__(
            fqdn,
            username,
            password,
            version)
        
        self.os_info = os_info
        self.vm_name = vm_name
        self.connection_server = connection_server
        self.build = None

        self.log.debug('RemoteEndpointBase: New %s instance created!' % (
                                    self.__class__.__name__))
        

    def update_pcoip_software(self, build):
        """
        Update the remote endpoint's PCoIP software (agent/firmware) to the specified build
        
        Arguments: 
            build - pcoip build to be installed on the endpoint
        Exceptions:
            UpdateError(description)
        """
        raise Exception('update_pcoip_software must be implemented in the concrete class!')
            
    def get_pcoip_version(self):
        """
        Returns PCoIP software/firmware version for the endpoint
        
        Similar functions:
            swift SwiftServer.get_pcoip_version()
        """
        raise Exception('get_pcoip_version must be implemented in the concrete class!')
