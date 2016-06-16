import socket
import array
import pickle

def start(argv):
    """Funkcja uruchamiająca klienta wysyłającego tabele odnosnie jakie ma zasoby oraz jakich bedzie potrzebowal

    Argumenty:
    argv - Argument sprawdzajacy czy zostal podany adres ip serwera.
    """
    if argv == '-1':
        hostname = input('Podaj  adres ip:  ')
    else:
        hostname = argv
    s = socket.socket()
    port = 9876
    allocated = [0,0,0,0]
    max = [0,0,0,0]
    i = 0
    while i < 4:
        m = input('Podaj '+str(i+1)+' element tabeli potrzebnych zasobow (beda 4):')
        a = input('Podaj '+str(i+1)+' element tabeli posiadanych zasobow (beda 4):')
        allocated[i] =int(a)
        max[i] = int(m)
        i+=1
    sendArray = allocated+max
    s.connect((hostname,port))
    s.send(pickle.dumps(sendArray))
    a=s.recv(1024)
    print (a)
    s.close
