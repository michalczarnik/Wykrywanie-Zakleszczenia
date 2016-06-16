import socket
import array
import pickle

def start(argv):
    if argv == '-1':
        hostname = input('Podaj  adres ip:  ')
    else:
        hostname = argv
    s = socket.socket()
    port = 9876
    allocated = array.array('i', [3,2,3,2])
    max = array.array('i', [4,5,6,5])
    sendArray = allocated+max
    s.connect((hostname,port))
    s.send(pickle.dumps(sendArray))
    a=s.recv(1024)
    print (a)
    s.close
