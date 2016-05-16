class TastLogger(object):
    '''
    TastLogger
    '''
    def __init__(self, name):
        self.name = name
    
    def log(self, message):
        print( 
            '[%s]: %s' % (
                self.name,
                message))
    
    def debug(self, message):
        '''
        '''
        self.log('debug: %s' % message)
                
    def info(self, message):
        '''
        '''
        self.log('info: %s' % message)
                
    def warning(self, message):
        '''
        '''
        self.log('warning: %s' % message)
                
    def error(self, message):
        '''
        '''
        self.log('error: %s' % message)
