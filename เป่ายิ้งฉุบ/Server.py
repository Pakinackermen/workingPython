import socket
import threading
import time
import random

def thread_client(con, address):
    msg = ' Welcome to PAO YING CHUP '.center(40, '#')
    msg2 = "You choose Hammer Paper or Scissors and server too, Who's gonna win. Good luck"
    msg3 = "Start in 3...2...1...Go !!!"
    con.send(msg.encode())
    time.sleep(1)
    con.send(msg2.encode())
    time.sleep(1)
    con.send(msg3.encode())
    time.sleep(1)
    round = 0
    win = 0
    loose = 0
    draw = 0
    while True:
        round_start = " ROUND {0} ".format(round+1).center(20,"*")
        con.send(round_start.encode())
        choice = ['HAMMER', 'PAPER', 'SCISSORS']
        choose = random.choice(choice)
        print(choose)
        select = con.recv(1024).decode()
        if select == '0':
            end_game = "Total time(s) you play: {0}\nWin: {1}\nLoose: {2}\nDraw: {3}\nGood Bye".format(round, win, loose,draw)
            con.send(end_game.encode())
            con.close()
            break

        elif select == '1':
            time.sleep(0.5)
            if choose == "HAMMER":
                result = "Server choose {0}\nResult: DRAW".format(choose)
                con.send(result.encode())
                draw += 1
            elif choose == "PAPER":
                result = "Server choose {0}\nResult: YOU LOOSE".format(choose)
                con.send(result.encode())
                loose += 1
            elif choose == "SCISSORS":
                result = "Server choose {0}\nResult: YOU WIN".format(choose)
                con.send(result.encode())
                win += 1
            round += 1

        elif select == '2':
            time.sleep(0.5)
            if choose == "HAMMER":
                result = "Server choose {0}\nResult: YOU WIN".format(choose)
                con.send(result.encode())
                win += 1
            elif choose == "PAPER":
                result = "Server choose {0}\nResult: DRAW".format(choose)
                con.send(result.encode())
                draw += 1
            elif choose == "SCISSORS":
                result = "Server choose {0}\nResult: YOU LOOSE".format(choose)
                con.send(result.encode())
                loose += 1
            round += 1

        elif select == '3':
            time.sleep(0.5)
            if choose == "HAMMER":
                result = "Server choose {0}\nResult: YOU LOOSE".format(choose)
                con.send(result.encode())
                loose += 1
            elif choose == "PAPER":
                result = "Server choose {0}\nResult: YOU WIN".format(choose)
                con.send(result.encode())
                win += 1
            elif choose == "SCISSORS":
                result = "Server choose {0}\nResult: DRAW".format(choose)
                con.send(result.encode())
                draw += 1
            round += 1
        else:
            time.sleep(0.5)
            pass
    con.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 12345
    s.bind((host, port))
    s.listen(2)
    while True:
        con, address = s.accept()
        t1 = threading.Thread(target=thread_client, args=(con, address))
        t1.start()

    s.close()

if __name__ == '__main__':
    main()
