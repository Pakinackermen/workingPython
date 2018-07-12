import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '127.0.0.1'
port = 12345

s.connect((server, port))
welcome_message = s.recv(1024).decode()
print(welcome_message)
name = input('Enter name: ')
s.send(name.encode())

start_chat = s.recv(1024).decode()
print(start_chat)
while True:
    message = input("Say something: ")
    s.send(message.encode())
    if message != 'exit':
        server_msg = s.recv(1024).decode()
        print(server_msg)
    else:
        print("Good bye")
        break
s.close()

