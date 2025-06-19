"""
endpoint.py
"""
from logger import TastLogger
from remote_machine import RemoteMachine

class EndpointBase(RemoteMachine):
    """
    Endpoint base class. Provides common endpoint functionality
    """

    def __init__(
        self, 
        fqdn, 
        username,
        password,
        version):
        """
        Arguments:
            fqdn: same as for RemoteMachine
            username: same as for RemoteMachine
            password: same as for RemoteMachine
            version: type specific, could include build information, we can use
                also values 'latest_dev', 'latest_released', etc.
        """

        self.log = TastLogger(self.__class__.__name__)
        self.log.debug('EndpointBase: Creating new %s instance...' % (
                                    self.__class__.__name__))

        super(EndpointBase, self).__init__(
            fqdn, 
            username,
            password)
            
        self.version = version

        self.log.debug('EndpointBase: New %s instance created!' % (
                                    self.__class__.__name__))
        
        