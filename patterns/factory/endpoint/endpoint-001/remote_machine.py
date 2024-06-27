"""
remote_machine.py

Provides functions for doing various operations on a remote machine (e.g. file
and directory operations, creating and managing processes, working with registry
etc.)
"""

# Imports
from logger import TastLogger
# Concrete remote machine classes
try:
    from remote_machine_wmi import RemoteMachine as WmiRemoteMachine
except Exception, e:
    print '*DEBUG* Unable to import remote_machine_wmi! (%s)' % str(e)
    WmiRemoteMachine = None
    
try:
    from remote_machine_ssh import RemoteMachine as SshRemoteMachine
except Exception, e:
    print '*DEBUG* Unable to import remote_machine_ssh! (%s)' % str(e)
    SshRemoteMachine = None


class RemoteMachine(object):
    """
    Provides functions for doing various operations on a remote machine (e.g. file
    and directory operations, creating and managing processes, working with registry
    etc.)
    
    This is factory class which creates and returns object of one of concrete
    classes (see list of concrete classes in the import section).
    
    For the list and documentation of the avaialable remote operations refer to
    the _RemoteMachineBase class.
    """

    def __init__(
        self, 
        fqdn='', 
        username='teralab', 
        password='tera%%lab', 
        *args, 
        **kwargs):
        """
        Arguments:
            fqdn: machine fqdn
            username: user of the machine, can be in the format 'domain\username'
            password: user's password
        """
        self.log = TastLogger(self.__class__.__name__)
        self.log.debug('RemoteMachine: Creating new %s instance...' % (
                                    self.__class__.__name__))
        
        rm = None
        
        if WmiRemoteMachine:
            try:
                rm = WmiRemoteMachine(fqdn, username, password)
            except Exception, e:
                self.log.debug('Unable to access machine %s using wmi. %s' % (fqdn, str(e)))
                rm = None
        else:
            self.log.debug('wmi is not available for accessing machine %s.' % fqdn)
                
        if rm is None:
            if SshRemoteMachine:
                try:
                    rm = SshRemoteMachine(fqdn, username, password)
                except Exception, e:
                    self.log.debug('Unable to access machine %s using ssh. %s' % (fqdn, str(e)))
                    rm = None
            else:
                self.log.debug('ssh is not available for accessing machine %s.' % fqdn)
                
        if rm is None:
            self.log.warning(
                'Unable to access machine %s remotely. '
                'No suitable remote protocol is available' % fqdn)
                
        self._remote_machine_obj = rm
        
        self.log.debug('RemoteMachine: New %s instance created!' % (
                                    self.__class__.__name__))
        

        
    def __getattr__(self, attr):
        """
        Invokes specified attribute implentation of the concrete class.
        """
        return getattr(self._remote_machine_obj, attr)

if __name__ == '__main__':
    rm = RemoteMachine('qe-016-win7-32.teradici.local', 'teraauto', 'tera%%lab')
    rm.start_process('notepad.exe')
