#!/usr/bin/python
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input('Enter your host IP: ')
port =input('Please enter port number:')
portNumber = int(port);
#if len(sys.argv) != 2:
#    print("Invalid Arguments")
#    exit(1)
#host = sys.argv[0]
# Connect the socket to the port where the server is listening
server_address = (host, portNumber)
print("server address is ", server_address)
sock.connect(server_address)

try:
    # Send data
    message = 'This is the message.'
    fileName = input('Please enter file name')
    request = 'GET '+ fileName + ' HTTP/1.0\r\n\r\n'
    sock.sendall(request.encode('utf-8'))
    # Look for the response
    amount_received = 0
    amount_expected = len(fileName)
    #while amount_received < amount_expected:
    #   data = sock.recv(24) 
      #  amount_received += len(data)
    #print("received %s", data);

finally:
    print("closing socket")
    sock.close()