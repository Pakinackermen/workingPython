import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host = ''
port = 12344

s.bind((host,port))

print('Server started')

while True:
    print("Waiting...")
    data, address = s.recvfrom(1024)
    print("from client: {}".format(address))
    print('Data: {0}'.format(data.decode()))
    msg = "Welcome to GONGA server"
    s.sendto(msg.encode(),address)
s.close()