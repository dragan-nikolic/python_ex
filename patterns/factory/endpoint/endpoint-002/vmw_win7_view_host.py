from logger import TastLogger
from remote_endpoint_base import RemoteEndpointBase


class VmwWin7ViewHost(RemoteEndpointBase):
    '''
    '''
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
        self.log.debug('VmwWin7ViewHost: Creating new %s instance...' % (
                                    self.__class__.__name__))
        
        super(VmwWin7ViewHost, self).__init__(
            fqdn,
            username,
            password,
            version,
            os_info,
            vm_name,
            connection_server)
        
        self.log.debug('VmwWin7ViewHost: New %s instance created!' % (
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
            'VmwWin7ViewHost %s:%s:%s updated to %s!' % (
                self.fqdn,
                self.connection_server,
                self.vm_name,
                str(build)))
            
    def get_pcoip_version(self):
        """
        Returns PCoIP software/firmware version for the endpoint
        
        Similar functions:
            swift SwiftServer.get_pcoip_version()
        """
        return self.build
