from local_endpoint import LocalEndpoint, LocalEndpointType, ConnectionInterface
from remote_endpoint import RemoteEndpoint, RemoteEndpointType

from logger import TastLogger

def main():
    lep = LocalEndpoint(
        'lep-fqdn001', 
        'teraauto', 
        'tera%%lab', 
        LocalEndpointType.VMW_VIEW_CLIENT,
        '1.2')
    rep = RemoteEndpoint(
        'rep-fqdn001',
        'teralab',
        'terapassword',
        RemoteEndpointType.VMW_WIN7_VIEW_HOST,
        '2.04',
        {'os': 'windows', 'os_ver': '7'},
        'vm_dnikolic_w7',
        'conn-server1')
    lep.connect_to_remote_endpoint(
        rep,
        ConnectionInterface.GUI,
        {'desktop_layout': 'fullscreen'}) 
    lep.start_process('notepad')
    lep.disconnect_from_remote_endpoint()

if __name__ == '__main__':
    main()