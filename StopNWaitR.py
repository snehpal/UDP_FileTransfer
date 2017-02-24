#!/usr/bin/env python
#importing different modules
import socket
import sys
import base64
#Passing argument for port number
host=''
port=int(sys.argv[1])
#Making a socket
try :
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ('Success: Socket created')
except socket.error:
    print ("Failure to make a socket")
    sys.exit
#Binding a socket
server.bind((host,port))
print("Socket has been binded")

#Defining some variables
FLAG='ACK'
#Receiving the SYN packet from sender
s = server.recvfrom(999999)
data = s[0]
#Decoding and splitting by |||
a=data.decode("utf8")
b=a.split('|||')
address = s[1]
    
print ("a is:" +a)
print(b[0])
print(b[1])
print(b[2])
    #print (b[3])
#If a SYN packet is received, empty file is made and ACK is send
if b[1]=="SYN":
    print ("Begin receiving: ",b[2])
    open("Received-"+b[2],'wb')
    x=(str(b[0])+'|||'+str(FLAG))
    print (x)
    ack=x.encode("utf8")
    print (ack) 
    server.sendto(ack, address)    
else:
    print ("File Not Received")
              
#Data packets are received and decoded
while True:
    s1 = server.recvfrom(999999)
    data = s1[0]
    a1=data.decode("utf8")
    b1=a1.split('|||')
    address = s1[1]
    print(b1[0])
    print(b1[1])
    print(b1[2])
    m=b1[1]
    m=m.encode("utf8")
    m=base64.b64decode(m)
    
#Data packets are written onto that empty file
    if b1[0]=="1" and b1[1]!="SYN":
        file=open("Received-"+b[2],"ab")
        file.write(m)
        #file.close()  
        x1=(str(b1[0])+'|||'+str(FLAG))
        print (x1)
        ack1=x1.encode("utf8")
        print (ack1) 
        server.sendto(ack1, address)
#FIN packet is received and an acknowledgement of ACK is send        
    if b1[1]=="b'FIN'":
        file.close()
        x2=(str("0")+'|||'+str(FLAG))
        print (x2)
        ack2=x2.encode("utf8")
        print (ack2) 
        server.sendto(ack2, address)
        print (b[2]+" Received.")  
        