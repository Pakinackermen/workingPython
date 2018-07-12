import socket
import threading
import time
from random import randint

def thread_client(con, address):
    welcome_message = '############Welcome to Less or More############'.center(40, '=')
    sec = 1
    time.sleep(sec)
    con.send(welcome_message.encode())
    hello_message = 'Server will random a number what you have to do is Guest the number and server will tell you its Less or More. Good luck '
    time.sleep(sec)
    con.send(hello_message.encode())
    start_message = 'Start in 3....2...1...GO!!!'

    time.sleep(sec)
    con.send(start_message.encode())
    while True:
        random = (randint(0, 100))
        print(random)
        while True:
            number = con.recv(1024).decode()
            n = int(number)


            if n < random :
                less_msg = 'Your number is Less T-T'
                con.send(less_msg.encode())

            elif n > random :
                less_msg = 'Your number is More T-T'
                con.send(less_msg.encode())

            elif n == random :
                less_msg = 'BINGO'
                con.send(less_msg.encode())
                break

        again = con.recv(1024).decode()
        if again == 'y':
            print("")
        else:
            break
    con.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '203.209.49.46'
    port = 12345
    s.bind((host, port))
    s.listen(2)
    print('Server started')
    while True:
        print('Waiting...')
        con, address = s.accept()
        print('connected from {}:{}'.format(address[0], address[1]))
        t1 = threading.Thread(target=thread_client, args=(con, address))
        t1.start()
    s.close()

if __name__ == '__main__':
    main()