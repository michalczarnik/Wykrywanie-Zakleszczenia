import socket
import array
import pickle

s = socket.socket()
host = socket.gethostname()
port = 9876

# s.connect((host, port))
s.connect(('192.168.0.12',port))
s.send('Siemka1'.encode())
s.send('Siemka2'.encode())
a=pickle.loads(s.recv(1024))
print (a)
print(a.count(3))
s.close
