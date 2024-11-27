from socket import *

# define addr: server do not need to define IP address, but client need.
serverPort = 12001
# define server socket
serverSocket = socket(AF_INET,SOCK_DGRAM) 
serverSocket.bind(('',serverPort))   # 服务器套接字（serverSocket）绑定到特定的地址和端口，以便能够接收来自客户端的连接请求

print("The server is ready!")
while True:
    msg, clientAddr = serverSocket.recvfrom(2048)
    mosifiedMsg = msg.decode().upper() # decode：convert bit to string
    serverSocket.sendto(mosifiedMsg.encode(),clientAddr)



   