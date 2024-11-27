# UDP -- no connection needed
# TCP -- need connection, more realiable

from socket import *

serverName = 'localhost'  
serverPort = 12001
serverAddr = (serverName,serverPort)

# set up a UDP socket: 
clientSocket = socket(AF_INET,SOCK_DGRAM)   #AF_INET:ipv4, SOCK_DGRAM:UDP

msg = input("Enter a lowercase sentence:")
clientSocket.sendto(msg.encode(),serverAddr)  # encode function:convert message to binary
modifiedMsg,addr = clientSocket.recvfrom(2048)    # modifiedMsg is binary
print(modifiedMsg.decode())    # decode(): convert binary to string
clientSocket.close()   # we need to close the socket