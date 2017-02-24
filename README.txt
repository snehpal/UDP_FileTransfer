This is a Stop-and-Wait Protocol implementation code. We implement this protocol over UDP sockets for reliable transmission of data. Stop-and-wait protocol also can be referred as Alternating bit protocol.
This method is used to send information	between two connected devices. It ensures that information is not lost due to dropped packets and that packets are received in the correct order. 
It is the simplest kind of automatic repeat-request (ARQ) method. A stop-and-wait ARQ sender sends one frame at a time; it is a special case of the general sliding window protocol with both transmit and receive window sizes equal to 1 and more than one respectively . 
After sending each frame, the sender doesn't send any further frames until it receives an acknowledgement (ACK) signal. After receiving a good frame, the receiver sends an ACK. 
If the ACK does not reach the sender before a certain time, known as the timeout, the sender sends the same frame again. Timer is set after each frame transmission. 
The above behavior is the simplest Stop-and-Wait implementation.
Now, we explain the code as per the sender and the receiver.
Sender:
First, we import the necessary modules required such as socket, sys, time, etc. Then, we define the host address, port and the filename as arguments that are to be passed via the command line.
A socket is created by giving the command- client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM). DGRAM means this socket will follow UDP implementation.
We find the length of the contents of the file. We define some flags and other initials. Encode some of them by converting them to bytes. 
We write a variable with seqeunce number, flag and filename in it. The variable is in strings and delimited by |||. Then, we encode this variable into bytes and send it to the receiver with the hostname and address.
Now, we receive an ackonwledgment from the receiver. It has a encoded variable which we decode into strings and then, split them by the ||| function.
If we receive ACK0, then, we start sending the file in packets of 1024. These packets are encoded into base64 and then, we add it to a variable which has a sequence number and data. This variable is further encoded into bytes.
We give a timeout of 500ms, after which if an acknowledgment hasn't been received it resends a packet. We send the file to the receiver with same hostname and port.
If the sender is done sending a file, it sends FIN acknowledgment to indicate to the receiver that it is done sending. We encode the variable with a sequence number and send it to the receiver.
It receives the FIN-ACK acknowledgement from the sender and sends one last ACK acknoledgement to the receiver and prints out the message that the file has been successfully send to the receiver.

Receiver:
First, we import the necessary modules required such as socket, sys, etc. Then, we define the port as argument that are to be passed via the command line.
A socket is created by giving the command- server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM). DGRAM means this socket will follow UDP implementation.
Then, we bind the socket to the host and the port. We define some flags and other initials. Encode some of them by converting them to bytes.
Now, we receive the variable from sender and decode it. We split it by the ||| function. If we find the SYN packet in it, we open a empty file into which we will write the following data. 
We send an acknowlegment ACK0 back to the sender. We encode the flag and sequence number into bytes and send it. 7
After receiving the ACK0 packet, the sender starts sending packets of file in 1024 size. We receive packets of these file, open them and write them into the file. 
For every packet of data received, we send an ACK back to the sender, who waits for the data and will retransmit if it doesnt receive the acknowledgment.
If the receiver receives a packet of FIN, it sends out an acknowledgement of FIN-ACK and sends it back to sender. 
If the receiver receives an ACK back, it prints out the message that the file has been received and terminates the connection.