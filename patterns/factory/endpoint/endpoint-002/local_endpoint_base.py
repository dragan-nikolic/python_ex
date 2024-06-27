"""
local_endpoint_base.py

abstract class that defines LocalEndpoint interface
"""
from endpoint_base import EndpointBase

from logger import TastLogger


class LocalEndpointBase(EndpointBase):
    """
    LocalEndpoint class provides functions for managing local PCoIP endpoint.
    """

    def __init__(
        self, 
        fqdn, 
        username, 
        password,
        version):
        """
        Arguments:
            fqdn: same as for Endpoint
            username: same as for Endpoint
            password: same as for Endpoint
            version: same as for Endpoint
        """

        self.log = TastLogger(self.__class__.__name__)
        self.log.debug('LocalEndpointBase: Creating new %s instance...' % (
                                    self.__class__.__name__))
                                    
        super(LocalEndpointBase, self).__init__(
            fqdn,
            username,
            password,
            version)

        self.connection_interface = None
        
        self.local_endpoint = None

        self.log.debug('LocalEndpointBase: New %s instance created!' % (
                                    self.__class__.__name__))

    # ===== session related functions =====

    def connect_to_remote_endpoint(
        self,
        remote_endpoint,
        connection_interface,
        configuration):
        """
        Arguments:
            RemoteEndpoint remote_endpoint: endpoint to connect to
            string connection_interface: 'ui' (sikuli) or 'api' (cmicl)
            dict configuration: parameters that depend on the client, server and
                connection interface types. For example, when using VMware View
                Client one parameter could be desktop layout (fullscreen or
                window with sepcific size); e.g. dictionary {'desktop_layout': 'fullscreen'}
        Exceptions:
            ConnectionError(description)
        """
        raise Exception('connect_to_remote_endpoint must be implemented in the concrete class!')


    def disconnect_from_remote_endpoint(self, method):
        """
        Arguments: method - e.g. disconnect, disconnect&logoff, tsdiscon, ctrl+alt+F12, etc
        Returns: none
        Exceptions:
            DisconnectionError(description)
        """
        raise Exception('disconnect_from_remote_endpoint must be implemented in the concrete class!')

