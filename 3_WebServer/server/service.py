from http.handle_requests import handle_user_request
from server.server_requests_logger import ServerRequestLogger

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

import socket
import sys
from thread import *

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8181  # Arbitrary non-privileged port


# Function for handling connections. This will be used to create threads
def client_thread(conn, client_ip, client_port):
    # Receiving from client, handle request and back the resposne
    data = conn.recv(1024)
    reply = handle_user_request(data, client_ip=client_ip, client_port=client_port)
    if data:
        conn.sendall(reply)

    conn.close()

def run_local_server():
    print 'Socket created'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        _run_server(s)
    except:
        pass
    s.close()

def _run_server(s):
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
        conn, address = s.accept()
        client_ip, client_port = address

        #start new thread takes 1st argument as a function name to be run_server, second is the tuple of arguments to the function.
        start_new_thread(client_thread, (conn, client_ip, client_port))
