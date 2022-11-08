import socket
import sys
sys.path.insert(0,"./src/protos")
from protos.messages_robocup_ssl_wrapper_pb2 import SSL_WrapperPacket

ip = '224.5.23.2'
port = 10006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 128)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)
sock.bind((ip, port))

data = sock.recvfrom(1024)
decode_data = SSL_WrapperPacket.FromString(data)
print(decode_data)
