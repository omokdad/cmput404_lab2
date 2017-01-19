#!/usr/bin/env python

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serverSocket.bind(("0.0.0.0",8000))

serverSocket.listen(5)

while True:
    (incomingSocket, address) = serverSocket.accept()
    print "Got a connection from %s" % (repr(address))
    
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET = IPv4
    # SOCK_STREM = TCP
    
    clientSocket.connect(("www.google.com",80))    
    
    request = bytearray()
    
    while True:
        part = incomingSocket.recv(1024)
        if (part):
            request.extend(part)
            clientSocket.sendall(part)
        else:
            break   
        
    print request