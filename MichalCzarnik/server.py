import socket
import time
import threading
import sys
import array
import pickle
import bankers

#Inicjalizacja zmiennych
number_of_connections = 0
allocationSuccessfull = 0
required_number_of_connections = 0

bankersFinished = False
allocated = []
max = []
resources= [ 3,1, 1, 2 ]


def start(argv):
    global required_number_of_connections
    if argv is -1:
        required_number_of_connections = input('Podaj ilosc wymaganych polaczen: ')
    else:
        required_number_of_connections = argv
    i=0
    while i<int(required_number_of_connections):
        allocated.append([])
        max.append([])
        i+=1

    s=socket.socket()
    host = socket.gethostname()
    port = 9876
    s.bind((host, port))
    wait = 0
    s.listen(5)
    while wait < int(required_number_of_connections):
        c, addr = s.accept()
        wait+=1
        try:
            t=threading.Thread(target=threadFunction, args=(c, addr))
            t.start()
        except:
            print ("Error: "+str(sys.exc_info()))

#Definicja funkcji wątku dla kazdego polaczenia
def threadFunction( c, addr):
    global number_of_connections
    conn_nr = number_of_connections
    recvArray = pickle.loads(c.recv(1024))
    aloc,maxi = split_list(recvArray)
    global required_number_of_connections
    print('Polaczenie nr: ',conn_nr+1)
    global bankersFinished
    global allocationSuccessfull
    for x in aloc:
        allocated[int(conn_nr)].append(x)
    for x in maxi:
        max[int(conn_nr)].append(x)
    number_of_connections+=1
    while number_of_connections < int(required_number_of_connections):
        time.sleep(0.1)
    if int(conn_nr==0):
        allocationSuccessfull = bankers.allocate(allocated,max,resources)
        bankersFinished=True
    while not bankersFinished:
        time.sleep(0.1)
    if allocationSuccessfull is 1:
        c.send('Nie wykryto zakleszczenia')
    else:
        c.send('Wykryto zakleszczenie'.encode())
    c.close()
    print('Zamknieto polaczenie nr ', conn_nr+1)

# Definicja funkcji dzilacej listy na pol
def split_list(a_list):
    half = len(a_list)/2
    return a_list[:int(half)], a_list[int(half):]
