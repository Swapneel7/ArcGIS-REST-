#!/usr/bin/python
import socket
import sys
import os
from pathlib import Path

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input('Enter your host IP: ')
port =input('Please enter port number:')
portNumber = int(port);

if not host or not port
    print("Invalid arguments ")
    exit(1)

# Bind the socket to the port
server_address = (host, portNumber)
print("starting server up on port ", server_address)
sock.bind(server_address)
print("Server listening....")

# Listen for incoming connections
sock.listen(5)

while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    
    try:
       # print >>sys.stderr, 'connection from', client_address
       # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(24)
            print("received %s" ,data)
            #if data:
             #   print("sending data back to the client")
             #   connection.sendall(data)
            #else:
             #   print("no more data from", client_address)
             #   break
            filename=data
            requestReceived = Path(filename.decode("utf-8"))
            print(filename)

            #Validate request format
            token0,token1,token2 = data.decode("utf-8").split(' ')
           
            if token0 != 'GET' or token2 != 'HTTP/1.0':
                print("HTTP/1.0 400 Bad Request \r\n\r\n")
            my_file=token1
            print(my_file)
            statinfo = os.stat(my_file)
            response =statinfo.st_size
            
            if my_file.is_file():
                f = open(filename,'rb')
                l = f.read(1024)
                msg = "HTTP/1.0 200 OK\r\n"
                connection.sendall(msg.encode("utf-8"))
                while (1):
                    connection.send(l.encode("utf-8"))
                    print('Sent ',repr(l))
            else:
                print("HTTP/1.0 400 Not Found\r\n\r\n")
            
            l = f.read(1024)
            f.close()
    
        connection.send("Thank you for connecting")
        
    finally:
        # Clean up the connection
        connection.close()
