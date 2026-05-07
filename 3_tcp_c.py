import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a TCP socket
dest_ip = '127.0.0.1' # destination ip address 
dest_port = 12345 # destination port number
s.connect((dest_ip, dest_port)) # connect to the server 

msg = input("Message to send: ") # get user input for the message to send to the server
while not msg == 'quit': # loop until the user types 'quit'
    s.send(bytes(msg, 'utf-8')) # send the message to the server, encoding it as bytes
    data = s.recv(4096) # receive data from the server, with a buffer size of 4096 bytes
    print("Server sent: ", data.decode('utf-8')) # decode the received bytes back to a string and print it
    msg = input("Message to send: ") # get user input for the next message to send to the server

s.close() # close the socket connection when done