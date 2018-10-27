# Python TCP Client A
import socket 



port = 2004
BUFFER_SIZE = 2000
ip_address = '127.0.0.1'
MESSAGE = raw_input("tcpClientA: Enter message/ Enter exit:")

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((ip_address, port))

while MESSAGE != 'exit':
    tcpClientA.send(MESSAGE)     
    data = tcpClientA.recv(BUFFER_SIZE)
    print " ClientA received data:", data
    MESSAGE = raw_input("tcpClientA: Enter message to continue/ Enter exit:")

tcpClientA.close() 