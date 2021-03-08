import socket
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print(sys.path)
sys.path.append('../')
from Client.AppConstants import *
from Client.clientController import *

class ClientService:    
    host = HOST
    port = PORT
    clientController = ClientController()

    def connectClientToServer(self):
        try:
            clientSocket=socket.socket()
            clientSocket.connect((self.host, self.port))
            print("Connected to server")
        except:
            print("Could not connect to server")
        finally:
                return clientSocket
    
    def getWelcomeMessageFromServer(self,clientSocket):
        jsonWelcomeResponse = self.clientController.receiveMessageFromServer(clientSocket)
        print(jsonWelcomeResponse['data'])

    def communicateWithServer(self,clientSocket):
        try:        
            while True:
                clientMessage = input("enter message to send: ")
                self.clientController.sendMessageToServer(clientSocket,clientMessage)
                if clientMessage.lower() == TERMINATE:
                    break
        except:
            print("Connection broken.")
    

def main():
    client=ClientService()
    clientSocket=client.connectClientToServer()
    client.getWelcomeMessageFromServer(clientSocket)
    client.communicateWithServer(clientSocket)

main()
