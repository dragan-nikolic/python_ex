import socket
import sys

def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

port = int(sys.argv[1])    
print(f'port {port} is in use: {is_port_in_use(port)}')
