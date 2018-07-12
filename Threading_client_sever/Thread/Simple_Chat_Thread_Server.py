import socket
import threading
import time

def thread_client(con, address):
    welcome_message = 'Welcome to Alpaca Server'.center(40, '=')

    con.send(welcome_message.encode())
    name = con.recv(1024).decode()
    start_chat = 'Hello, {}. CHAT started'.format(name.upper().center(50,'*'))
    con.send(start_chat.encode())

    while True:
        message = con.recv(1024).decode()
        print(message)
        if message != 'exit':
            server_msg = 'server say : {} on {}'.format(message.upper(),time.strftime("%m/%d/%y %H:%M:%S"))
            con.send(server_msg.encode())
        else:
            print("Close connection")
            break
    con.close()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
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
        t1.join()

    s.close()


if __name__ == '__main__':
    main()