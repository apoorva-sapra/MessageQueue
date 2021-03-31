from datetime import datetime, timedelta
from ImqServer.Server.Storage.DatabaseHandler import *
from ImqServer.Server.ServerMessageController import *
from ImqServer.Server.AppConstants import *
from ImqServer.Server.MessageQueue.MessagePacket import *
from ImqServer.Server.MessageQueue.Queue import *
import sys
import os
sys.path.append('../')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class PublisherHandler:
    __databaseHandler = DatabaseHandler()
    __serverMessageController = ServerMessageController()
    queueObject = ""
    __topicName = ""
    __messageToPublish = ""

    def handlePublishRequest(self, clientSocket, messageToPublish, topicName, queue):
        self.queueObject = queue
        self.__topicName = topicName
        self.__messageToPublish = messageToPublish
        self.__databaseHandler.connectWithDatabase()

        self.__databaseHandler.insertDataInClientMessageTable(messageToPublish, topicName)
        self.insertDataInMessageQueue()

        self.__serverMessageController.sendMessageToClient(clientSocket, MESSAGE_PUBLISHED)

    def insertDataInMessageQueue(self):
        messagePacket = self.createMessagePacket()
        self.AddMessagePacketInQueue(messagePacket)

    def getCurrentTime(self):
        currentTime = datetime.now()
        return currentTime

    def createMessagePacket(self):
        messageArrivalTime = self.getCurrentTime()
        lastMessageId = self.__databaseHandler.getLastMessageId()
        messagePacket = MessagePacket(self.__topicName, self.__messageToPublish, messageArrivalTime)
        messagePacket.messageId = lastMessageId
        return messagePacket

    def AddMessagePacketInQueue(self, messagePacket):
        self.queueObject.queue.append(messagePacket)

    def getUpdatedQueue(self):
        return self.queueObject
        
