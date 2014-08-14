__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

import socket
import sys
from thread import *

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8181  # Arbitrary non-privileged port


# Function for handling connections. This will be used to create threads
def client_thread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n')  #send only takes string

    #infinite loop so that function do not terminate and thread do not end.
    while True:

        #Receiving from client
        data = conn.recv(1024)
        reply = data
        if not data:
            break

        conn.sendall(reply)

    #came out of loop
    conn.close()

def run():
    print 'Socket created'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        _run(s)
    except:
        pass
    s.close()

def _run(s):
    #Bind socket to local host and port
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
    except socket.error, msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    print 'Socket bind complete'

    #Start listening on socket
    s.listen(10)
    print 'Socket now listening'

    #now keep talking with the client
    while 1:
        #wait to accept a connection - blocking call
        conn, addr = s.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])

        #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
        start_new_thread(client_thread, (conn,))
