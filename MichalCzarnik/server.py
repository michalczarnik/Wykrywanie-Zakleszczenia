import socket
import _thread
import time

# Define a function for the thread
def print_time( threadName):
    c, addr = s.accept()
    print('Connected from ',addr)
    c.send('Thanks for connecting to server'.encode())
    c.close()

s=socket.socket()
host = socket.gethostname()
port = 9876
s.bind((host, port))

s.listen(5)
while True:
    try:
        _thread.start_new_thread( print_time, ("Thread-1",  ) )
    except:
        print ("Error: unable to start thread")

while 1:
   pass
