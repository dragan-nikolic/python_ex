"""
endpoint.py
"""
from logger import TastLogger
from remote_machine import RemoteMachine

class Endpoint(RemoteMachine):
    """
    Endpoint base class. Provides common endpoint functionality
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
            fqdn: same as for RemoteMachine
            username: same as for RemoteMachine
            password: same as for RemoteMachine
            type: one of LocalEndpointType or RemoteEndpointType values
            version: type specific, could include build information, we can use
                also values 'latest_dev', 'latest_released', etc.
        """

        self.log = TastLogger(self.__class__.__name__)
        self.log.debug('Endpoint: Creating new %s instance...' % (
                                    self.__class__.__name__))

        super(Endpoint, self).__init__(
            fqdn, 
            username,
            password)
            
        self.type = type
        self.version = version

        self.log.debug('Endpoint: New %s instance created!' % (
                                    self.__class__.__name__))
        
        