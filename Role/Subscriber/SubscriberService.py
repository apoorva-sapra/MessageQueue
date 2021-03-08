import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Storage.DatabaseHandler import *
from Server.ServerController import *


class SubscriberService:

    __clientConnection = ""
    __clientName = ""
    __topicID = 0
    __databaseController = DatabaseHandler()
    __messageList = ""
    communicationController = ServerController()

    def __init__(self, clientConnection, clientName, topicID):
        self.__clientConnection = clientConnection
        self.__clientName = clientName
        self.__topicID = topicID
        

    def connectWithDatabase(self):
        self.__databaseController.initDatabaseConnection()

    def createSubscriberTopicTable(self):
        self.__databaseController.createSubscriberTopicTable()

    def createSubscriberMessageMappingTable(self):
        self.__databaseController.createSubscriberMessageMappingTable()

    def addDataInSubscriberTopicTable(self):
        self.__databaseController.saveSubscriberTopicDataInTable(self.__clientName, self.__topicID)

    def fetchDataFromMessageTable(self):
        self.__messageList = self.__databaseController.fecthDataFromMessageTable(self.__topicID)
        
    def sendMessagesToClient(self):
        self.communicationController.sendMessageToClient(self.__clientConnection, self.__messageList)
