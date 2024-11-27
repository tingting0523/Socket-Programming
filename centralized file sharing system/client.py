'''
Script for client side
'''
import protocol
import config
from socket import *
import os
from pathlib import Path
import shutil

class client:
    
    fileList=[] # list to store the file information

    #Constructor: load client configuration from config file
    def __init__(self):
        self.serverName, self.serverPort,self.clientPort, self.downloadPath, self.uploadPath = config.config().readClientConfig()
        self.serverPath = config.config().readServerConfig()

    # Function to produce user menu 
    def printMenu(self):
        print("Welcome to simple file sharing system!")
        print("Please select operations from menu")
        print("--------------------------------------")
        print("1. Review the List of Available Files")
        print("2. Download File")
        print("3. Upload File")  #Tingting
        # *******************************
        # ADD one line here for uploading files
        print("4. Quit")

    # Function to get user selection from the menu
    def getUserSelection(self):        #Tingting
        ans=0
        # only accept option 1-4
        # ******************************
        # When you add upload option, you need to modify the number of options
        # you accept
        while ans>4 or ans<1:
            self.printMenu()
            try:
                ans=int(input())
            except:
                ans=0
            if (ans<=4) and (ans>=1):
                return ans
            print("Invalid Option")

    # Build connection to server
    def connect(self):
        serverName = str(self.serverName)
        serverPort = int(self.serverPort)
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        return clientSocket

    # Get file list from server by sending the request
    def getFileList(self):
        mySocket=self.connect()
        mySocket.send(protocol.prepareMsg(protocol.HEAD_REQUEST," "))
        header, msg=protocol.decodeMsg(mySocket.recv(1024).decode())
        mySocket.close()
        if(header==protocol.HEAD_LIST): 
            files=msg.split(",")
            self.fileList=[]
            for f in files:
                self.fileList.append(f)
        else:
            print ("Error: cannnot get file list!")

    # function to print files in the list with the file number
    def printFileList(self):
        count=0
        for f in self.fileList:
            count+=1
            print('{:<3d}{}'.format(count,f))

    # Function to select the file from file list by file number,
    # return the file name user selected
    def selectDownloadFile(self):
        if(len(self.fileList)==0):
            self.getFileList()
        ans=-1
        while ans<0 or ans>len(self.fileList)+1:
            self.printFileList()
            print("Please select the file you want to download from the list (enter the number of files):")
            try:
                ans=int(input())
            except:
                ans=-1
            if (ans>0) and (ans<len(self.fileList)+1):
                return self.fileList[ans-1]
            print("Invalid number")

    # Function to send download request to server and wait for file data
    def downloadFile(self,fileName):
        mySocket=self.connect()
        mySocket.send(protocol.prepareMsg(protocol.HEAD_DOWNLOAD, fileName))
        with open(self.downloadPath+"/"+fileName, 'wb') as f:
            print ('file opened')
            while True:
                #print('receiving data...')
                data = mySocket.recv(1024)
                #print('data=%s', (data))
                if not data:
                    break
            # write data to a file
                f.write(data)
        print(fileName+" has been downloaded!")
        mySocket.close()
 
    #********************************************
    # Please complete the upLoadFile function, the function takes a file name as
    # an input
    def uploadFile(self,fileName):
        file_path = Path(self.uploadPath) / fileName
        if not file_path.exists():
            print(f"File '{file_path}' does not exist!")
            return
        mySocket = self.connect()
        mySocket.send(protocol.prepareMsg(protocol.HEAD_UPLOAD, fileName))
        with open(file_path, 'rb') as f:
            while chunk := f.read(1024):  
                mySocket.send(chunk)
        mySocket.close()


    #********************************************
    # Please complete the select Upload file function,
    # The function should print out a list of files from upload folder for user to
    # select, and user need to chose one file.
    # The reture value should be a file name

    def selectUploadFile(self):
        upload_dir = Path(self.uploadPath)
        if not upload_dir.exists():
            print(f"Upload directory '{upload_dir}' does not exist!")
            return None
    
        upload_files = [f for f in upload_dir.iterdir() if f.is_file()]
    
        if not upload_files:
            print("No files available in the upload directory.")
            return None
    
        print("Files available for upload:")
        for idx, file in enumerate(upload_files, 1):
            print(f"{idx}. {file.name}")

        while True:
            try:
                choice = int(input("Select a file to upload (enter the file number): "))
                if 1 <= choice <= len(upload_files):
                    selected_file = upload_files[choice - 1]
                    target_dir = Path(self.serverPath[1])  
                    target_file_path = target_dir / selected_file.name
                    shutil.copy(selected_file, target_file_path)
                    print(f"File '{selected_file.name}' has been uploaded to '{target_dir}'")
                    return selected_file.name
            except ValueError:
                pass
            print("Invalid choice, please try again.")
         
    # Main logic of the clien, start the client application
    def start(self):
        opt=0
        while opt!=3:
            opt=self.getUserSelection()
            if opt==1:
                if(len(self.fileList)==0):
                    self.getFileList()
                self.printFileList()                  
            elif opt==2:
                self.downloadFile(self.selectDownloadFile())
            elif opt==3:
                self.uploadFile(self.selectUploadFile())
            #**************************
            # You need another option for uploading files
            else:
                pass
                
def main():
    c=client()
    c.start()
main()
