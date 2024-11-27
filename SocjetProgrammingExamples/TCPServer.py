from socket import *


'''
def server(connectedSocket):
    msg = connection.recv(1024)
    mosifiedMsg = msg.decode().upper()
    connection.send(mosifiedMsg.encode())
    connection.close()
'''


# define addr: server do not need to define IP address, but client need.
# define server socket
serverPort=12003
serverSocket = socket(AF_INET,SOCK_STREAM)   #SOCK_STREAM：TCP as protocol
serverSocket.bind(('',serverPort))   # 服务器套接字（serverSocket）绑定到特定的地址和端口，以便能够接收来自客户端的连接请求
serverSocket.listen(20)   # 设置为监听状态，以便接受来自客户端的连接请求  1 means 1 connection   100:maxmum connections to handle

print("The server is ready!")
while True:
    connection, addr = serverSocket.accept()
    msg = connection.recv(1024)
    mosifiedMsg = msg.decode().upper()
    connection.send(mosifiedMsg.encode())
    connection.close()

''' multi connections
while True:
    connection, addr = serverSocket.accept()
    t=threading.Thread(target=service,argv=[connection])
    t.start()
'''
