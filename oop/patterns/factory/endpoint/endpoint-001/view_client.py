from logger import TastLogger

class ViewClient(object):
    '''
    ViewClient
    '''
    def __init__(self):
        """
        """

        self.log = TastLogger(self.__class__.__name__)
        self.log.debug('ViewClient: New %s instance created!' % (
                                    self.__class__.__name__))
        
        
    def start_view_client(
        self, 
        remote_endpoint,
        configuration):
        '''
        '''
        self.log.info(
            'view_client connected to %s with configurartion %s' % (
                str(remote_endpoint),
                str(configuration)))
                
    def close_view_client():
        self.log.info('view client closed!')