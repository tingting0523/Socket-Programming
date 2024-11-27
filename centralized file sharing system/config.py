'''
This is the file to read configuration files
Format of the server configuration file:
SERVER_PORT=SERVER_PORT_NUMBER
PATH=PATH_OF_SERVER_SHARED_DIRECTORY

Format of the client configuration file:
SERVER=SERVER_HOSTNAME/IP
SERVER_PORT=SERVER_PORT_NUMBER
CLIENT_PORT=CLIENT_PORT_NUMBER
DOWNLOAD=PATH_OF_CLIENT_DOWNLOAD_DIRECTORY
************************* ADD one varible of upload path
UPLOAD=PATH_OF_CLIENT_UPLOAD_DIRECTORY
'''
import os

class config:
    #define header
    server_port='SERVER_PORT'
    path="PATH"
    server="SERVER"
    client_port="CLIENT_PORT"
    download="DOWNLOAD"
    upload="UPLOAD"  # Tingting
    #serverConfig="server.config"
    serverConfig = os.path.join(os.path.dirname(os.path.abspath(__file__)), "server.config")
    clientConfig="client.config"
    
    def __init__(self):
        pass

    def readServerConfig(self):
        try:
            with open(self.serverConfig, 'r') as f:
                serPort = 0
                sharePath = ""
                for l in f:
                    sub = l.strip().split("=")
                    if sub[0] == self.server_port:
                        serPort = int(sub[1])
                    elif sub[0] == self.path:
                        sharePath = sub[1]
                if serPort == 0 or not sharePath:
                   raise ValueError("Invalid configuration: Missing SERVER_PORT or PATH")
                return int(serPort), sharePath
        except FileNotFoundError:
            print(f"Configuration file '{self.serverConfig}' not found.")
            exit(1)  # Exit the program if the configuration file is missing
        except ValueError as e:
            print(f"Error in configuration file: {e}")
            exit(1)  # Exit if the configuration is invalid
        except Exception as e:
            print(f"Unexpected error reading configuration: {e}")
            exit(1)
          
    def readClientConfig(self):
        '''
        This function read client configuration file, return four values
        @return: serverName
        @return: serverPort
        @return: clientPort
        @return: downloadPath
        @return: uploadPath
        '''
        try:
            with open(self.clientConfig,'r') as f:
                serPort=0
                clientPort=0
                downPath=""
                upPath=""
                for l in f:
                    sub=l.strip().split("=")
                    if(sub[0]==self.server_port):
                        serPort=int(sub[1])
                    elif(sub[0]==self.server):
                        serName=sub[1]
                    elif(sub[0]==self.client_port):
                        clientPort=sub[1]   
                    elif(sub[0]==self.download):
                        downPath=sub[1]  
                    elif(sub[0]==self.upload):
                        upPath=sub[1]    
                    else:
                        pass  
                return serName, serPort, clientPort, downPath, upPath
        except:
            print(Exception.message())
     
# The function to test the configuration class           
def test():
    conf=config()
    client=conf.readClientConfig()
    server=conf.readServerConfig()
    print(client)
    print(server)