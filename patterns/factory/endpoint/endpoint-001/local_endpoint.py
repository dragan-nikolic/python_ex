"""
local_endpoint.py

Provides functions for managing a local PCoIP endpoint

Usage:
    import endpoint
    from local_endpoint import LocalEndpoint
    from remote_endpoint import RemoteEndpoint

    lep = LocalEndpoint(
                'tervdiwin7p9.teradici.com',
                {'username': 'teraauto', 'password': 'terapass', 'domain': 'teradici'},
                endpoint.VMW_VIEW_CLIENT,
                '5.1',
                'kvmoip',
                'core-kvmoip-1')
    lep = RemoteEndpoint(
                '192.168.0.10',
                {'username': 'teraauto', 'password': 'terapass', 'domain': 'teradici'},
                endpoint.VMW_VIEW_AGENT,
                '5.2',
                {'os_name': 'WINDOWS', 'os_version': '6.1', 'theme': 'classic'},
                'auto_w7p32h',
                'conn_server1.teradici.local')
    lep.connect_to_remote_endpoint(rep, endpoint.USER_INTERFACE, {'desktop_layout': 'windowLarge'})
    lep.disconnect_from_remote_endpoint(endpoint.DISCONNECT_AND_LOGOFF)
"""
import endpoint

from logger import TastLogger

from view_client import ViewClient
from zero_client import ZeroClient

class ConnectionInterface:
    """
    Method to access a client
    """
    GUI = 'gui'  # access client via GUI (using e.g. Sikuli)
    API = 'api'  # access client via API (using e.g. CMICL, RPC)
    
class DesktopLayout:
    MULTIMONITOR = 'multimonitor'
    FULLSCREEN = 'fullscreen'
    WINDOW_SMALL = 'windowSmall'
    WINDOW_LARGE = 'windowLarge'
    WINDOW_SIZE = 'windowSize'

class LocalEndpointType:
    VMW_VIEW_CLIENT = 'vmw_view_client'
    TERA1_CLIENT = 'tera1_client'
    TERA2_CLIENT = 'tera2_client'
    TERADICI_WINDOWS_CLIENT = 'teradici_windows_client'
    ATLAS_CLIENT = 'atlas_client'

class LocalEndpoint(endpoint.Endpoint):
    """
    LocalEndpoint class provides functions for managing local PCoIP endpoint.
    """

    def __init__(
        self, 
        fqdn, 
        username, 
        password,
        type, 
        version,
        viewer_type,
        viewer_id):
        """
        Arguments:
            fqdn: same as for Endpoint
            username: same as for Endpoint
            password: same as for Endpoint
            type: one of LocalEndpointType values
            version: same as for Endpoint
            viewer_type: 'kvmoip' or 'dp-dvi'
            viewer_id: type specific, for 'kvmoip' switch it is fqdn or ipaddr
                of the kvmoip device
        """

        self.log = TastLogger(self.__class__.__name__)
        self.log.debug('LocalEndpoint: Creating new %s instance...' % (
                                    self.__class__.__name__))
                                    
        super(LocalEndpoint, self).__init__(
            fqdn,
            username,
            password,
            type,
            version)

        self.viewer_type = viewer_type
        self.viewer_id = viewer_id
        self.connection_interface = None
        
        self._local_endpoint_obj = None

        self.log.debug('LocalEndpoint: New %s instance created!' % (
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
        Similar functions:
            softi PcoipClient.create_pcoip_session(pcoip_client, pcoip_server, *args)
            swift SwiftClient*.start_pcoip_session(desktop)+verify_session_start()
            swift SwiftSession.initialize()+create_pcoip_session()
            firmware SessionCtrl.start_session_direct()
        Questions:
            - How do we connect through security gateway? Is that defined by connection server?
        """

        self._connection_interface = connection_interface

        if ((self.type == LocalEndpointType.VMW_VIEW_CLIENT) and 
            (self._connection_interface == ConnectionInterface.GUI)):
            self._local_endpoint_obj = ViewClient()

            self._local_endpoint_obj.start_view_client(
                    remote_endpoint,
                    configuration)

        elif ((self.type == LocalEndpointType.TERA1_CLIENT) and 
              (self._connection_interface == ConnectionInterface.GUI)):
            self._local_endpoint_obj = ZeroClient()

            self._local_endpoint_obj.create_pcoip_session(
                    remote_endpoint,
                    configuration)

        else:
            self.log.error(
                'Unknown PCoIP client (%s) or connection interface (%s)' % (
                    self.type, 
                    self._connection_interface))


    def disconnect_from_remote_endpoint(self, method):
        """
        Arguments: method - e.g. disconnect, disconnect&logoff, tsdiscon, ctrl+alt+F12, etc
        Returns: none
        Exceptions:
            DisconnectionError(description)
        Simialar functions:
            softi PcoipClient.close_pcoip_session()
            swift SwiftClient*.terminate_pcoip_session()
            swift SwiftSession.close_pcoip_session()
            firmware SessionCtrl.stop_session()
        """
        if ((self.type == LocalEndpointType.VMW_VIEW_CLIENT) and 
            (self._connection_interface == ConnectionInterface.GUI)):

            self._local_endpoint_obj.close_view_client()
                
        elif ((self.type == LocalEndpointType.TERA1_CLIENT) and 
              (self._connection_interface == ConnectionInterface.GUI)):

            self._local_endpoint_obj.close_pcoip_session()
                    
        else:
            self.log.error(
                'disconnect_from_remote_endpoint is not implemented for %s client and %s interface!' % (
                    self.type, 
                    self._connection_interface))

if __name__ == '__main__':
    lep = LocalEndpoint(
        'lep-fqdn001', 
        'teraauto', 
        'tera%%lab', 
        LocalEndpointType.VMW_VIEW_CLIENT,
        '1.2',
        'DPCard_Viewer',
        'viewer-fqdn-001')
    rep = RemoteEndpoint(
        'rep-fqdn001',
        'teralab',
        'terapassword',
        Remote)
    lep.connect_to_remote_endpoint() 
 