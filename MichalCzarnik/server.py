import socket
import time
import threading
import sys
import array
import pickle

#Inicjalizacja zmiennych
number_of_connections = 0
required_number_of_connections = input('Podaj ilosc wymaganych polaczen: ')

#Definicja funkcji odpowiedzialnej za algorytm bankiera
def bankersAlgorithm():
    return 'asd'

#Definicja funkcji wątku dla kazdego polaczenia
def threadFunction( c, addr):
    a=array.array('i', [1,2,3,4])
    global number_of_connections
    conn_nr = number_of_connections
    recvArray = pickle.loads(c.recv(1024))
    need,need2 = split_list(recvArray)
    print(str(recvArray)+' = '+str(need)+' + '+str(need2))
    global required_number_of_connections
    print('Polaczenie nr: ',conn_nr+1)
    number_of_connections+=1
    while number_of_connections < int(required_number_of_connections):
        time.sleep(0.1)
    bankersAlgorithm()
    c.send(pickle.dumps(a))
    c.close()
    print('Zamknieto polaczenie nr ', conn_nr+1)

# Definicja funkcji dzilacej listy na pol
def split_list(a_list):
    half = len(a_list)/2
    return a_list[:int(half)], a_list[int(half):]

s=socket.socket()
host = socket.gethostname()
port = 9876
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    try:
        t=threading.Thread(target=threadFunction, args=(c, addr))
        t.daemon=True
        t.start()
    except:
        print ("Error: "+str(sys.exc_info()))

while 1:
   pass
