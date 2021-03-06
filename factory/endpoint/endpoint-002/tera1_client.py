from logger import TastLogger
from local_endpoint_base import LocalEndpointBase

class Tera1Client(LocalEndpointBase):
    '''
    '''
    def __init__(
        self, 
        fqdn, 
        username, 
        password,
        version):
        """
        """
        self.log = TastLogger(self.__class__.__name__)
        self.log.debug('Tera1Client: Creating new %s instance...' % (
                                    self.__class__.__name__))
                                    
        super(Tera1Client, self).__init__(
            fqdn,
            username,
            password,
            version)
            
        self.connection_interface = None

        self.log.debug('Tera1Client: New %s instance created!' % (
                                    self.__class__.__name__))
        
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
        self.log.info(
            'tera1 client %s connected to %s via %s with configurartion %s' % (
                self.fqdn,
                str(remote_endpoint),
                str(connection_interface),
                str(configuration)))


    def disconnect_from_remote_endpoint(self, method):
        """
        Arguments: method - e.g. disconnect, disconnect&logoff, tsdiscon, ctrl+alt+F12, etc
        Returns: none
        Exceptions:
            DisconnectionError(description)
        """
        self.log.info('tera1 client %s closed!' % self.fqdn)
