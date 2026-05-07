#include <iostream>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>

using namespace std;

int main() {

    const char* ip_address = "127.0.0.1"; // IP address of the server
    const int port_no = 5555; // port number on which the server is listening

    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0) {
        perror("error creating socket");
    }

    struct sockaddr_in sin;
    memset(&sin, 0, sizeof(sin));
    sin.sin_family = AF_INET;
    sin.sin_addr.s_addr = inet_addr(ip_address);
    sin.sin_port = htons(port_no);

    char data[] = "hello"; // data to be sent to the server
    int data_len = sizeof(data);

    int sent_bytes = sendto(sock, data, data_len, 0, (struct sockaddr *) &sin, sizeof(sin)); // sendto() is used for UDP sockets
    if (sent_bytes < 0) {
        perror("error writing to socket");
    }

    struct sockaddr_in from;
    unsigned int from_len = sizeof(struct sockaddr_in);
    char buffer[4096]; // buffer to hold the response from the server
    int bytes = recvfrom(sock, buffer, sizeof(buffer), 0, (struct sockaddr *) &from, &from_len); // recvfrom() is used for UDP sockets
    if (bytes < 0) {
        perror("error reading from socket");
    }

    cout << "The server sent: " << buffer << endl;

    close(sock); // close the socket

    return 0;
}