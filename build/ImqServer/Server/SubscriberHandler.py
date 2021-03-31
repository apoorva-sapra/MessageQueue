from ImqServer.Server.Storage.DatabaseHandler import *
from ImqServer.Server.ServerMessageController import *
from ImqServer.Server.AppConstants import *
from ImqServer.Server.MessageQueue.QueueHandler import QueueHandler
import sys
import os
sys.path.append('../')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class SubscriberHandler:
    __clientId = 0
    __topicName = ""
    __topicId = 0
    __messages = []
    __clienSocket = ""
    __queueHandler=QueueHandler()
    databaseHandler = DatabaseHandler()
    serverMessageController = ServerMessageController()

    def handleSubscribeRequest(self, clientSocket, clientName, topicName, queue, deadLetterQueue):
        self.databaseHandler.connectWithDatabase()
        self.__clientId = self.databaseHandler.getClientId(clientName)
        self.__topicName = topicName
        self.__topicId = self.databaseHandler.getTopicId(topicName)
        self.__clientSocket = clientSocket
        self.queueObject=queue
        self.deadLetterQueueObject=deadLetterQueue
        self.getSubscribedMessages()

    def getSubscribedMessages(self):
        self.handleDeadMessagesInQueue()
        if not self.databaseHandler.checkClientAndTopicExistInMessageMapping(self.__clientId, self.__topicId):
            self.__messages=self.getMessagesFromQueue()
            if not self.__messages:
                # Retrieveing data from DATABASE when queue fails
                self.__messages = self.databaseHandler.getMessagesFromClientMessageTable(
                self.__topicId)
                pass
            if self.__messages:
                lastSeenMessageId = self.getLastSeenMessageId()
                self.databaseHandler.addDataInMessageMappingTable(self.__clientId, self.__topicId, lastSeenMessageId)
        else:
            lastSeenMessageId = self.databaseHandler.getLastSeenMessageIdFromMessageMappingTable(
                self.__topicId, self.__clientId)       
            self.__messages = self.getUnseenMessagesFromQueue(lastSeenMessageId)
            if not self.__messages:
                # Retrieveing Unseen messages from DATABASE when queue fails
                self.__messages = self.databaseHandler.getUnseenMessagesFromDatabase(
                lastSeenMessageId, self.__topicId)
            if self.__messages:
                lastSeenMessageId = self.getLastSeenMessageId()
                self.databaseHandler.updateLastSeenMessageId(lastSeenMessageId, self.__clientId, self.__topicId)
        self.sendMessagesToClient()

    def getLastSeenMessageId(self):
        lengthOfMessages = len(self.__messages)
        return self.__messages[lengthOfMessages-1][1]

    def sendMessagesToClient(self):
        self.serverMessageController.sendMessageToClient(
            self.__clientSocket, self.__messages)

    def getMessagesFromQueue(self):
        messages=[()]
        for eachMessagePacket in self.queueObject.queue:
            if eachMessagePacket.topicName == self.__topicName:
                messages.append((eachMessagePacket.data,eachMessagePacket.messageId))
        del messages[0]
        return messages

    def getUnseenMessagesFromQueue(self,lastSeenMessageId):
        messages=[()]
        for eachMessagePacket in self.queueObject.queue:
            if eachMessagePacket.topicName == self.__topicName:
                if eachMessagePacket.messageId > lastSeenMessageId:
                    messages.append((eachMessagePacket.data,eachMessagePacket.messageId))
        del messages[0]
        return messages

    def handleDeadMessagesInQueue(self):
        self.__queueHandler.handleMessageQueue(self.queueObject,self.deadLetterQueueObject)