import socket
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('../')
from ImqClient.Client.AppConstants import *
from ImqClient.Client.ClientMessageController import *
from ImqClient.Client.Exception.ClientException import *
from ImqClient.Client.Exception.ExceptionConstants import *

class ClientService:    
    host = HOST
    port = PORT
    clientMessageController = ClientMessageController()
    clientRole=""
    topicName=""
    clientSocket=""

    def connectClientToServer(self):
        try:
            self.clientSocket=socket.socket()
            self.clientSocket.connect((self.host, self.port))
            print(SERVER_CONNECTED)
        except:
            raise CouldNotConnectToServerException(SERVER_UNAVAIALBLE)
    
    def getWelcomeMessageFromServer(self):
        jsonWelcomeResponse = self.clientMessageController.receiveMessageFromServer(self.clientSocket)
        print(jsonWelcomeResponse[DATA])

    def displayHelpString(self):
        print(HELP_STRING)

    def communicateWithServer(self):
        try:   
            clientName = input(ENTER_USERNAME_STRING)  
            self.clientMessageController.sendMessageToServer(self.clientSocket,clientName)
            self.displayHelpString()
            while True:
                inputCommand = input(COMMAND)
                if inputCommand.lower() == TERMINATE:
                    self.clientMessageController.sendMessageToServer(self.clientSocket,inputCommand)              
                    break
                self.implementClientAction(inputCommand)
        except:
            raise DefaultException(DEFAULT_EXCEPTION_MESSAGE)

    def implementClientAction(self,inputCommand):
        clientAction = self.getClientAction(inputCommand)
        try:
            if clientAction == CONNECT:
                self.implementConnectAction(inputCommand)  
            
            if clientAction == ADD:
                self.implementAddAction(inputCommand) 

            if ((clientAction == PUBLISH or clientAction == SUBSCRIBE) and (self.topicName == "")):
                print(FIRST_CONNECT_TO_TOPIC_MESSAGE)
            
            if ((clientAction == PUBLISH) and (not self.topicName.isspace()) and (self.topicName)):
                self.implementPublishAction(inputCommand)

            if clientAction == SUBSCRIBE and self.topicName != "":
                self.implementSubscribeAction()

            if clientAction == MANUAL:
                print(HELP_STRING)
        except:
            raise CommandParserException(INVALID_COMMAND)

    def implementConnectAction(self,inputCommand):
        self.topicName = self.getTopic(inputCommand)
        try:
            if self.topicName and not self.topicName.isspace():
                self.sendTopicToConnectToServer(self.topicName)
                print(self.clientMessageController.receiveMessageFromServer(self.clientSocket)[DATA])
        except:
            raise CommandParserException(INVALID_COMMAND)


    def implementAddAction(self,inputCommand):
        try:
            self.topicName = self.getTopic(inputCommand)
            if self.topicName and not self.topicName.isspace():
                self.sendTopicToAddToServer(self.topicName)
                print(self.clientMessageController.receiveMessageFromServer(self.clientSocket)[DATA])
        except:
            raise CommandParserException(INVALID_COMMAND)

    def implementPublishAction(self,inputCommand):
        try:
            messageToPublish = self.getMessageToPublish(inputCommand)
            if messageToPublish and not messageToPublish.isspace():
                self.sendMessageToPublishToServer(messageToPublish)
        except:
            raise CommandParserException(INVALID_COMMAND)

    def implementSubscribeAction(self):
        self.clientMessageController.sendMessageToServer(
            self.clientSocket,message=PULL, request= SUBSCRIBE)
        subscriberJsonResponse=self.clientMessageController.receiveMessageFromServer(self.clientSocket)
        self.displaySubscribedMessages(subscriberJsonResponse[DATA])
    
    def displaySubscribedMessages(self,subscriberJsonResponse):
        for eachResponse in subscriberJsonResponse:
            print(eachResponse[0])
        
    def getClientAction(self,inputCommand):
        try:
            if inputCommand.split(' ')[0] != IMQ:
                raise Exception
            else: 
                clientAction = inputCommand.split(' ')[1]
                if clientAction in CLIENT_ACTIONS and not clientAction.isspace():
                    return clientAction
                raise Exception
        except:
            print(INVALID_COMMAND)
            

    def getTopic(self,inputCommand):
        try:
            topicName = inputCommand.split()[2]
            return topicName
        except:
            raise CommandParserException(INVALID_COMMAND)
    
    def getMessageToPublish(self,inputCommand):
        try:
            messageToPublish = inputCommand.split('-m')[1].split("\"")[1]
            return messageToPublish
        except:
            raise MessageNotProvidedException(MESSAGE_NOT_PROVIDED)

    def sendMessageToPublishToServer(self,messageToPublish):
        self.clientMessageController.sendMessageToServer(
                self.clientSocket, messageToPublish, request= PUBLISH)
        publishStatus=self.clientMessageController.receiveMessageFromServer(self.clientSocket)
        print(publishStatus[DATA])

    def sendTopicToConnectToServer(self,topicName):
        self.clientMessageController.sendMessageToServer(
            self.clientSocket, topicName)

    def sendTopicToAddToServer(self,topicName):
        self.clientMessageController.sendMessageToServer(
            self.clientSocket, topicName, request=ADD)
