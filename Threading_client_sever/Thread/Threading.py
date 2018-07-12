import time
import threading

def timer(name,delay,repeat):
    print(' Timer No. {} Start '.format(name).center(30, '-'))
    for i in range(repeat):
        time.sleep(delay)
        print('No: {} : {}'.format(name, time.time()))
    print(' Timer No. {} Stop '.format(name).center(30, '-'))

def main():
    # timer('01',1,5)
    # timer('02', 0.5, 5)

    t1 = threading.Thread(target=timer,args=('01',1,3))
    t2 = threading.Thread(target=timer,args=('04',0.5,6))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('Main Finish')
if __name__ == '__main__':
    main()