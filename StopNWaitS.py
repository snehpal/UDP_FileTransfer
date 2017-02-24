#!/usr/bin/env python
#Importing different modules
import socket
import sys
import os.path
import base64
import time
import random
import base64
#Passing arguments for filename, hostname and port number
host = sys.argv[2]
port = int(sys.argv[3])
filename=sys.argv[1]
#Making a socket
try:
    client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print ("Failure to make a socket")
    sys.exit
#Defining some variables
i=0
u=os.path.getsize(filename)
sequence_number=1
sn=0
FLAG="SYN"
FLAG1="ACK"
FLAG1=FLAG1.encode("utf8")
E_FLAG="FIN"
E_FLAG=E_FLAG.encode("utf8")
l=0
q=(str(sn)+'|||'+str(FLAG)+'|||'+str(filename)+'|||'+str(l))
#Encoding and sending SYN packet 
f=q.encode("utf8")
client.sendto(f,(host,port))
#Receiving data and splitting it by |||
feedback=client.recvfrom(66534)

d=feedback[0]
a=feedback[1]
print("Server responds: ", d)
a=d.decode("utf8")
b=a.split('|||')
print(a)
print(b)
print(b[0])
print(b[1])
#Sending data packets
if b[1]=="ACK" and b[0]=="0":
    while i!=u:
        with open(filename, 'rb') as file:
            try:
                file.seek(i)
                data = file.read(1024)
                i=file.tell()
                m=base64.b64encode(data).decode()
                print(i)
                print ('data', m)
                at=(str(sequence_number)+'|||'+m+'|||'+str(l))
                print (at)
                
                file_send=at.encode("utf8")
#Implementing a timeout
                time.sleep(0.005)
                print (file_send)
                k=random.randint(0,100)
                if (i>10):
                    client.sendto(file_send,(host,port))
                
            except socket.error:
                print ("File Not send")
#Sending a FIN packet to alert the receiver that the file has ended                
    if i==u:
        y=(str(sn)+'|||'+str(E_FLAG)+'|||'+str(l))
        print (y)
        file_end=y.encode("utf8")
        print(file_end)
        client.sendto(file_end,(host,port))
#Receiving a ACK packet as an acknowledgement send by receiver after which the client terminates
        fe=client.recvfrom(66534)
        d2=fe[0]
        a2=fe[1]
        a2=d2.decode("utf8")
        b2=a2.split('|||')
        print(b2[1])
        if b2[1]=="ACK":        
            print (filename+" is successfully sent to "+host+":"+str(port))