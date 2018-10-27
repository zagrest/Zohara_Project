# Python TCP Client B
import socket 


port = 2004
BUFFER_SIZE = 2000
ip_address = '127.0.0.1'
MESSAGE = raw_input("tcpClientB: Enter message/ Enter exit:")
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect((ip_address, port))

while MESSAGE != 'exit':
    tcpClientB.send(MESSAGE)     
    data = tcpClientB.recv(BUFFER_SIZE)
    print " ClientB received data:", data
    MESSAGE = raw_input("tcpClientB: Enter message to continue/ Enter exit:")

tcpClientB.close() 