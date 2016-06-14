import socket
import array
import pickle

s = socket.socket()
host = socket.gethostname()
port = 9876

need = array.array('i', [3,2,3,2,3])
need2 = array.array('i', [4,5,6,5,6])
sendArray = need+need2
# print (str(need)+' + '+str(need2)+' = ' + str(sendArray))
s.connect(('192.168.0.12',port))
s.send(pickle.dumps(sendArray))
a=pickle.loads(s.recv(1024))
print (a)
s.close
