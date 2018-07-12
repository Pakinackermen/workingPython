import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '203.209.49.46'
port = 12345

s.connect((server, port))
welcome_message = s.recv(1024).decode()
print(welcome_message)

hello_message = s.recv(1024).decode()
print(hello_message)

start_message = s.recv(1024).decode()
print(start_message)

while True:
    number = input('Enter number[1-100]: ')
    s.send(number.encode())

    less_msg = s.recv(1024).decode()


    if less_msg == 'BINGO':
        print(less_msg)


        again = input('Do you want to play again[Y/N] :')
        if again == 'y':
            s.send(again.encode())

        elif again == 'n':
            print("Good bye")
            break

    else:
        print(less_msg)



s.close()