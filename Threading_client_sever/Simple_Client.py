import socket
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345

s.connect((host, port))

welcome_message = s.recv(1000).decode()
print(welcome_message)


name = input('Enter a name : ')

s.send(name.encode())

#wel_msg = s.recv(1024).decode()
#symbol = s.recv(1024).decode()
print(s.recv(1024).decode())
print(s.recv(1024).decode())
#print("{0} {1}".format(wel_msg))
