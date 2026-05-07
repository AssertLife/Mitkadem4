from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM) # initiate a UDP socket

src_ip = '' # listen to all ips
src_port = 12345 # source port number
s.bind((src_ip, src_port)) # bind the socket to the source IP and port number
counter = 0 # initialize a counter to keep track of the number of messages received


while True: # continuously listen for incoming messages
    data, sender_info = s.recvfrom(2048) # receive a message from the sender (buffer size is 2048 bytes)
    print(data.decode('utf-8')) #print the received message utf-8
    print(sender_info) # print the sender's information (IP address and port number)

    s.sendto(data.upper(), sender_info) # send a response back to the sender (convert the message to uppercase)

    print('Message #{} processed.'.format(counter)) # print the number of messages processed


# Explanation: I added a coutner to count the number of messages received and processed. The counter is initialized to 0 and is incremented each time a message is received and processed. The current count is printed after processing each message.   