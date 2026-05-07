import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP/IP socket
server_ip = '' # Listen on all interfaces
server_port = 12345 # Port to listen on
server.bind((server_ip, server_port)) #  binds the socket
server.listen(5) # Listen for incoming connections, with a backlog of 5

while True: # Server loop to accept and handle incoming connections
    client_socket, client_address = server.accept() # Accept a new connection
    print('Connection from: ', client_address) # Print the address of the connected client
    data = client_socket.recv(1024) # Receive data from the client (up to 1024 bytes)
    while not data.decode('utf-8') == '': # Loop to handle client communication until the client disconnects
        print('Received: ', data.decode('utf-8')) # Print the received data from the client
        client_socket.send(data.upper()) # Send the received data back to the client in uppercase
        data = client_socket.recv(1024) # Wait for more data from the client
 
    print('Client disconnected') # Print a message when the client disconnects
    client_socket.close() # Close the client socket after the client disconnects