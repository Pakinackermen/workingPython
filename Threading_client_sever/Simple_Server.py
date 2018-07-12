import socket
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM)
host = ''
port = 12345

s.bind((host, port))
s.listen(5)

print('Server Start')

while True:
    print('Waiting...')
    con, address = s.accept()
    print('Connected')

    welcome_message = 'Welcome To SERVER'

    con.send(welcome_message.encode())

    name = con.recv(1024).decode()
    wel_msg = 'Hello, {}'.format(name.upper())

    con.send(wel_msg.encode())
    n = ''
    for i in range(0, len(name) + 1):
        n = n + "*" * i + "\n"
    con.send(n.encode())