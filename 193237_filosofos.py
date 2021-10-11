import time
from threading import *
from collections import deque
import threading
quiet = Lock()

def main ():
    filosofo1 = Thread(name='1',target=accion, args=())
    filosofo1.start()
    filosofo2 = Thread(name='2',target=accion, args=())
    filosofo2.start()
    filosofo3 = Thread(name='3',target=accion, args=())
    filosofo3.start()
    filosofo4 = Thread(name='4',target=accion, args=())
    filosofo4.start()
    filosofo5 = Thread(name='5',target=accion, args=())
    filosofo5.start()

def accion():
    fork = deque()
    forks = fork.copy()
    for i in range(0, 3): 
        forks.append(i)
    current = threading.current_thread().getName()
    while True:
        print('Filósofo #', current, 'esperando.')
        time.sleep(2)
        quiet.acquire()
        if len(forks) != 0:
            print('\nFilósofo #', current, 'toma 2 tenedores.')
            time.sleep(2)
            fork.append(forks.pop())
            fork.append(forks.pop())
            
        try:
            if len(fork)==2:
                print('Filósofo #', current, 'esta comiendo.')   
                time.sleep(3) 
                forks.append(fork.pop())
                forks.append(fork.pop())
        finally:
            print('Filósofo #', current, 'termino de comer.')         
            time.sleep(2)
            quiet.release()
            break

main()