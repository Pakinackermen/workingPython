import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '127.0.0.1'
port = 12345

s.connect((server, port))

msg = s.recv(1024).decode()
print(msg)
msg2 = s.recv(1024).decode()
print(msg2)
msg3 = s.recv(1024).decode()
print(msg3)

while True:
    round_start = s.recv(1024).decode()
    print(round_start)
    select = input("1.HAMMER 2.PAPER 3.SCISSORS 0.Exit, Select : ")
    print("-" * 30)
    if select == "0":
        s.send("0".encode())
        print("-" * 30)
        end_game = s.recv(1024).decode()
        print(end_game)
        s.close()
        break
    elif select == "1":
        s.send("1".encode())
        result = s.recv(1024).decode()
        print(result)
    elif select == "2":
        s.send("2".encode())
        result = s.recv(1024).decode()
        print(result)
    elif select == "3":
        s.send("3".encode())
        result = s.recv(1024).decode()
        print(result)
    else:
        pass
