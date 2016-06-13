import socket
import _thread
import time
import threading
import sys

i=1
# Define a function for the thread
def print_time( c, addr):
    print('Connected from ',addr)
    global i
    print(i)
    i+=1
    c.send('Thanks for connecting to server'.encode())
    c.close()
    time.sleep(5)
    print(i)
    print('Connection Closed ',addr)


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
        # _thread.start_new_thread( print_time, (c, addr ) )
    except:
        print ("Error: "+str(sys.exc_info()))

while 1:
   pass
