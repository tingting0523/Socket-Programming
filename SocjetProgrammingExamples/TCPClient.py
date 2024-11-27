# UDP -- no connection needed, faster
# TCP -- need connection, more realiable

from socket import *

# define server addr
serverName = 'localhost'
servertPort = 12003
serverAddr = (serverName,servertPort)

clientSocket = socket(AF_INET,SOCK_STREAM)      #TCP:SOCK_STREAM  UDP:SOCK_DGRAM

msg = input('Enter lowercase sentence:')
clientSocket.connect(serverAddr)
clientSocket.send(msg.encode())        # TCP just use send(), UDP need user sentto()
modifiedMsg = clientSocket.recv(1024)   # 1024: buffer size
print(modifiedMsg.decode())
clientSocket.close()   # we need to close the socket

