import socket
import time
import threading
import sys
import array
import pickle
import bankers

#Inicjalizacja zmiennych globalnych
number_of_connections = 0
allocationSuccessfull = 0
required_number_of_connections = 0
bankersFinished = False
allocated = []
max = []
resources= [ 0,0,0,0 ]
startTime = 0
endTime = 0

def start(argv):
    """Funkcja uruchamiająca serwer, po wprowadzeniu ilosci polaczen dla ktorych bedzie wykonywany algorytm tworzy dla kazdego nadchodzacego polaczenia osobny watek.

    Argumenty:
    argv - Argument sprawdzajacy czy wybrana zostala ilosc polaczen.
    """"
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
    i=0
    while i < 4:
        res = input('Podaj '+str(i+1)+' element tabeli posiadanych zasobow (beda 4):')
        resources[i] = int(res)
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

def threadFunction( c, addr):
    """Funkcja wykonywana przez kazde polaczenie przychodzace. Odpowiedzialna za odebranie danych przychodzacych od klienta, zapisanie ich do zmiennej globalnej, wykonaniu na niej algorytmu bankiera oraz odeslaniu informacji.

    Argumenty:
    c - Nowa inicjalizacja klasy Socket. Sluzy do wysylania i odbierania danych.
    addr - Adres klienta ktory sie polaczyl do serwera.
    """
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
    if int(conn_nr) is 0:
        global startTime
        startTime=time.time()
    if int(conn_nr==0):
        print(allocated)
        print(max)
        print(resources)
        allocationSuccessfull = bankers.allocate(allocated,max,resources)
        bankersFinished=True
    while not bankersFinished:
        time.sleep(0.1)
    if allocationSuccessfull is 1:
        c.send('Nie wykryto zakleszczenia'.encode())
    else:
        c.send('Wykryto zakleszczenie'.encode())
    c.close()
    print('Zamknieto polaczenie nr ', conn_nr+1)
    if int(conn_nr) is int(required_number_of_connections)-1:
        global endTime
        endTime = time.time()
        print('Czas wykonania : ' + str(endTime-startTime))

def split_list(a_list):
    """Funkcja dzielaca liste na pol. Potrzebna w celu rozdzielenia listy przychodzacej od klienta

    Argumenty:
    a_list - Lista która ma być podzielona

    Zmienne wyjsciowe:
    Dwie połowiczne listy
    """
    half = len(a_list)/2
    return a_list[:int(half)], a_list[int(half):]
