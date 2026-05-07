from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM) // initiate a UDP socket

dst_ip = '127.0.0.1' # destination IP address (localhost in this case)
dst_port = 12345 # destination port number

s.sendto(b'Hello', (dst_ip,dst_port)) # send a message to the destination

data, sender_info = s.recvfrom(2048) # receive a message from the sender (buffer size is 2048 bytes)
print(data.decode('utf-8')) # print the received message
print(sender_info) # print the sender's information (IP address and port number)

s.close() # close the socket
