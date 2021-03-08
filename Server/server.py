import socket
from _thread import start_new_thread 
import sys
import os
sys.path.append('../')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Server.AppConstants import *
from Storage.DatabaseHandler import * 
from Server.ServerController import *

class Server:

    ServerSocket = socket.socket()
    storage = DatabaseHandler()
    serverController = ServerController()

    def createServerSocket(self):
        return socket.socket()

    def bindServerSocket(self,serverSocket,host,port):
        try:
            serverSocket.bind((host, port))
        except socket.error as errorMessage:
            print(str(errorMessage))

    def setServerListener(self, serverSocket):
        serverSocket.listen(10)

    def acceptConnectionFromClient(self, serverSocket):
        return serverSocket.accept()

    def echoToClient(self,data,clientSocket):
        self.serverController.sendMessageToClient(clientSocket,serverReplyMessage+data)

    def sendWelcomeMessageToClient(self,clientSocket):
        self.serverController.sendMessageToClient(clientSocket,WELCOME)

    def storeClientRequest(self,clientSocket,clientName):
        print("enter store client req method")
        while True:
            self.storage.connectWithDatabase()
            self.storage.insertIntoReferenceTable(clientName)
            clientJsonMessageResponse = self.serverController.receiveMessageFromClient(
                clientSocket)
            print(clientJsonMessageResponse)
            data = clientJsonMessageResponse['data']
            print(data)
            self.storage.storeClientRequestInDatabase(clientName,data)
            if data.lower() == TERMINATE:
                break
            # data = clientSocket.recv(BUFFER).decode('utf-8')
            # self.storage.storeClientRequestInDatabase(clientName,data)
            # if data.strip().lower() == TERMINATE:
            #     break
        clientSocket.close()
            
    def establishConnectionWithClient(self,serverSocket):
            return serverSocket.accept()

    def getClientRoleJsonResponse(self,clientSocket):
        clientJsonRoleResponse = self.serverController.receiveMessageFromClient(
            clientSocket)
        print("client Role " + clientJsonRoleResponse['data'])
        return clientJsonRoleResponse

    def startNewClientThread(self,serverSocket):
        while True:
            clientSocket, address = self.establishConnectionWithClient(serverSocket)
            self.sendWelcomeMessageToClient(clientSocket)
          
            clientName = address[0] + '__' + str(address[1])
            print('Connected to',clientName)
            start_new_thread(self.storeClientRequest, (clientSocket,clientName))

def startServer():
    host = HOST
    port = PORT
    server=Server()
    serverSocket=server.createServerSocket()
    server.bindServerSocket(serverSocket,host,port)
    print('Server waiting for a Connection..')
    server.setServerListener(serverSocket)
    server.startNewClientThread(serverSocket)
    serverSocket.close()

startServer()
