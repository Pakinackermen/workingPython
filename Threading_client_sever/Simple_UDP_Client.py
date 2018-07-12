import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 12344

server = (host,port)

msg = 'Hello'

s.sendto(msg.encode(),server)

print(s.recvfrom(1024)[0].decode())

s.close()