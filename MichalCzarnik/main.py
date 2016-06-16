import server
import client
import sys
def helpMessage():
    "Zdefiniowana funkcja majaca na celu w razie wprowadzenia nieprawidlowych danych wejsciowych wypisze dostepne opcje"
    print('USAGE')
    print('\tUsage: program -server|-client [-n number] [-i ip adress] ')
    print('')
    print('where: ')
    print ('\t-server\t\t-\tStarting the server module')
    print ('\t-client\t\t-\tStarting the client module')
    print('')
    print('optional:')
    print ('\t-n number\t-\tNumber of connections (only usable in server module). If null taken from input.')
    print ('\t-i ip adress\t-\t IP Adress for server (only usable in client module). If null taken from input.')

if len(sys.argv) > 1:
    if sys.argv[1] == '-server':
        if len(sys.argv) >3:
            if  sys.argv[2] == '-n':
                if(isinstance(int(sys.argv[3]), int)):
                    server.start(sys.argv[3])
                else:
                    helpMessage()
        else:
            server.start(-1)
    elif sys.argv[1] == '-client':
        if len(sys.argv) >3:
            if sys.argv[2] == '-i':
                client.start(sys.argv[3])
        else:
            client.start('-1')
    else:
        helpMessage()
else:
    helpMessage()
