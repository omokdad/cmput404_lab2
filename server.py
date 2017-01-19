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
    
    incomingSocket.setblocking(0)  
    clientSocket.setblocking(0)    
    
    while True:
        request = bytearray()
        
        while True:
            try:
                part = incomingSocket.recv(1024)
            except IOError, e:
                if e.errno == socket.errno.EAGAIN:
                    break
                else:
                    raise
            if (part):
                request.extend(part)
                clientSocket.sendall(part)
            else:
                break   
            
        if len(request) > 0:    
            print request
        
        response = bytearray()
        
        while True:
            try:
                part = clientSocket.recv(1024)
            except IOError, e:
                if e.errno == socket.errno.EAGAIN:
                    break
                else:
                    raise
            if (part):
                response.extend(part)
                incomingSocket.sendall(part)
            else:
                break   
        if len(response) > 0:    
            print response