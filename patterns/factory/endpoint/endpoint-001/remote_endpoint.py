"""
remote_endpoint.py
"""

from logger import TastLogger

from endpoint import Endpoint


class RemoteEndpointType:
    VMW_VIEW_HOST = 'vmw_view_host'
    TERA1_HOST = 'tera1_host'
    TERA2_HOST = 'tera2_host'
    
class RemoteEndpoint(Endpoint):
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
        
        super(RemoteEndpoint, self).__init__(
            fqdn,
            username,
            password,
            type,
            version)
        
        self.os_info = os_info
        self.vm_name = vm_name
        self.connection_server = connection_server
        self.build = None

        self.log.debug('RemoteEndpoint: New %s instance created!' % (
                                    self.__class__.__name__))
        

    def update_pcoip_software(self, build):
        """
        Update the remote endpoint's PCoIP software (agent/firmware) to the specified build
        
        Arguments: 
            build - pcoip build to be installed on the endpoint
        Exceptions:
            UpdateError(description)
        """
        self.build = build
        
        self.log.info(
            'installed build %s on remote endpoint %s:%s' % (
                build,
                self.connection_server,
                self.vm_name))
            
    def get_pcoip_version(self):
        """
        Returns PCoIP software/firmware version for the endpoint
        
        Similar functions:
            swift SwiftServer.get_pcoip_version()
        """
        return self.build
