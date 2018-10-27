import socket 
from threading import Thread
import time



# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,conn,ip,port):
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port
        self.socket = conn
        print "[+] New server socket thread started for " + ip + ":" + str(port)
        fs = open('lofile-SERVER', 'a')  # open log file for debugging

        tcur = time.time()
        line = "\n [+] New server socket thread started for port,time" + ":" + str(port) + " " + str(tcur)
        fs.write(line)
        fs.close()


    def run(self):
        ITEM = 'null'
        while True :
            data = self.socket.recv(2048)
            f = open('lofile', 'a')  # open log file for debugging
            print "Server Thread received data ", port,data
            tcur = time.time()
            line = "\n Server Thread received data,port,time " + data + " " + str(port) + " " +  str(tcur)
            f.write(line)

            if (data.find("ENQ"))>= 0:
                data_state = 0
                Start = data.find("<")
                if Start == -1:
                    data_state = 1  # Not Found
                else:
                    data = data[Start+1:]
                    Start = data.rfind(">") #start from the end  to find the last occurence
                    if Start == -1:
                        data_state = 1  # Not Found
                    else:
                        data = data[0:Start]
                        data_state = 0

                if data_state == 1 or len(data)==0:
                    MESSAGE = "Error in Item"
                else:
                    ITEM = data  # save client item
                    MESSAGE = "OK"
            #end treatment of ENQ message

            elif (data.find("DEQ"))== 0:
                if ITEM=="null":
                    MESSAGE = "NULL ITEM"
                else:
                    MESSAGE = ITEM  # get client item

            else:
                MESSAGE = "ERROR - UNKNOWN MESSAGE"
            #end treatment of incoming message

            if MESSAGE == 'exit':
                break
            print "send msg" , MESSAGE
            self.socket.send(MESSAGE)
            tcur = time.time()
            line = "\n send msg : msg,port,time " + str(MESSAGE) + " " + str(port) + " " + str(tcur)
            f.write(line)
            f.close()  # close log file for debugging
           #time.sleep(0)  #NOT nessary to impose context switching


# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '127.0.0.1'
TCP_PORT = 2004 

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT))

threads = [] 
f = open('lofile', 'w')
f.write('start logger file\n')

while True: 
    tcpServer.listen(4) 
    print "Multithreaded Python server : Waiting for connections from TCP clients..." 
    (conn, (ip,port)) = tcpServer.accept()
    #conn.setblocking(0)
    newthread = ClientThread(conn,ip,port)
    newthread.start() 
    threads.append(newthread) 

 #AT THE VERY END - NOT IN USE
for t in threads:
    t.join()

