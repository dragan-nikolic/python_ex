from logger import TastLogger

class RemoteMachineBase(object):
    '''
    '''
    def __init__(
        self, 
        fqdn='', 
        username='', 
        password='', 
        **kwargs):
        
        self.log = TastLogger(self.__class__.__name__)
        self.log.debug('RemoteMachineBase: Creating new %s instance...' % (
                                    self.__class__.__name__))
        
       
        self.fqdn = fqdn
        self.username = username
        self.password = password

        self.log.debug('RemoteMachineBase: New %s instance created!' % (
                                    self.__class__.__name__))
        