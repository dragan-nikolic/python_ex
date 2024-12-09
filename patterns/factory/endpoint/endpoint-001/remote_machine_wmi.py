from logger import TastLogger

from remote_machine_base import RemoteMachineBase

class RemoteMachine(RemoteMachineBase):
    '''
    Class that wraps all the above Remote* classes. Use this class if you want
    all of the above functionality
    '''
    def __init__(
        self, 
        fqdn='', 
        username='', 
        password='', 
        **kwargs):
      
        self.log = TastLogger(self.__class__.__name__)
        self.log.debug('RemoteMachineWmi: Creating new %s instance...' % (
                                    self.__class__.__name__))
        
       
        super(RemoteMachine, self).__init__(
            fqdn, 
            username,
            password)
            
        self.log.debug('RemoteMachineWmi: New %s instance created!' % (
                                    self.__class__.__name__))
        

    def start_process(self, process_name):
        '''
        '''
        self.log.info('process %s started!' % process_name)
