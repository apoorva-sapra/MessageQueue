from Server.ServerController import *
# from Storage. import *
from Publisher.PublisherConstants import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class PublisherService:


    databaseController = DatabaseController()
    
    serverController = ServerController()

    def __init__(self, clientSocket, clientName, topicID):
        self.clientSocket = clientSocket
        self.clientName = clientName
        self.topicID = topicID

    def connectWithDatabase(self):
        self.__databaseController.initDatabaseConnection()

    def createPublisherTopicTable(self):
        self.__databaseController.createPublisherTopicTable()

    def addDataInTable(self):
        self.__databaseController.savePublisherTopicDataInTable(
            self.__clientName, self.__topicID)

    def publishDataInTable(self):
        try:
            while True:
                clientJsonMessageResponse = self.communicationController.receiveMessageFromClient(
                    self.__clientConnection)
                if clientJsonMessageResponse['data'].lower() == self.__EXIT:
                    break
                try:
                    self.__databaseController.saveDataInMessageTable(
                        self.__clientName, clientJsonMessageResponse['data'], self.__topicID)
                except Exception as e:
                    print(e)
                    exit()
                data = "server acknowledge"
                self.communicationController.sendMessageToClient(
                    self.__clientConnection, data)

        except ConnectionResetError as e:
            print("Connection is closed")
        except Exception as e:
            print(e)

        self.__clientConnection.close()
