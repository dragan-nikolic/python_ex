from logger import TastLogger

class ZeroClient(object):
    '''
    ZeroClient
    '''
    def __init__(self):
        """
        """

        self.log = TastLogger(self.__class__.__name__)
        self.log.debug('ZeroClient: New %s instance created!' % (
                                    self.__class__.__name__))
        
        
    def create_pcoip_session(
        self, 
        remote_endpoint,
        configuration):
        '''
        '''
        self.log.info(
            'zero_client connected to %s with configurartion %s' % (
                str(remote_endpoint),
                str(configuration)))
                
    def close_pcoip_session():
        self.log.info('pcoip session closed!')