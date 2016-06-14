import socket
import time
import threading
import sys
import array
import pickle



number_of_connections = 0
# Define a function for the thread
def print_time( c, addr):
    a=array.array('i', [1,2,3,4,3])
    print('Connected from ',addr)
    global number_of_connections
    number_of_connections+=1
    print(c.recv(1024))
    print(c.recv(1024))
    while number_of_connections < 1:
        time.sleep(0.1)
    c.send(pickle.dumps(a))
    print('Connection Closed ',addr)
    c.close()


s=socket.socket()
host = socket.gethostname()
port = 9876
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    try:
        t=threading.Thread(target=print_time, args=(c, addr))
        t.daemon=True
        t.start()
    except:
        print ("Error: "+str(sys.exc_info()))

while 1:
   pass
