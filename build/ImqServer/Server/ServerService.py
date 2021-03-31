from ImqServer.Server.Storage.DatabaseHandler import *
from ImqServer.Server.Storage.DatabaseConstants import *
from ImqServer.Server.PublisherHandler import PublisherHandler
from ImqServer.Server.SubscriberHandler import SubscriberHandler
from ImqServer.Server.ServerMessageController import *
from ImqServer.Server.AppConstants import *
from ImqServer.Server.MessageQueue.Queue import *
from ImqServer.Server.Protocol.ProtocolConstants import *
import socket
from ImqServer.Server.Exceptions.ServerException import *
from ImqServer.Server.Exceptions.ExceptionConstants import *
from _thread import start_new_thread
import sys
import os
sys.path.append('../')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class ServerService:
    __queue = ""
    __deadLetterQueue = ""
    __clientSocket = ""
    __clientName = ""
    __topicName = ""

    def __init__(self):
        self.serverSocket = self.createServerSocket()
        self.databseHandler = DatabaseHandler()
        self.serverMessageController = ServerMessageController()
        self.subscriberHandler = SubscriberHandler()
        self.publisherHandler = PublisherHandler()

    def createServerSocket(self):
        return socket.socket()

    def createClientSocket(self):
        self.__clientSocket, address = self.serverSocket.accept()

    def bindServerSocket(self, host, port):
        try:
            self.serverSocket.bind((host, port))
        except socket.error:
            raise SocketException(SOCKET_EXCEPTION_MESSAGE)

    def startServerListener(self):
        try:
            self.serverSocket.listen(10)
        except:
            raise ServerListenerException(SERVER_LISTENER_EXCEPTION_MESSAGE)

    def acceptConnectionFromClient(self):
        try:
            return self.serverSocket.accept()
        except:
            raise ServerAcceptorException(SERVER_ACCEPTOR_EXCEPTION_MESSAGE)

    def sendWelcomeMessageToClient(self):
        self.serverMessageController.sendMessageToClient(
            self.__clientSocket, WELCOME)

    def createTablesInDatabase(self):
        self.databseHandler.connectWithDatabase()
        self.databseHandler.createDatabaseTables()

    def AddTopicsInDatabase(self):
        self.databseHandler.AddTopicsInTopicTable()

    def AddRolesInDatabase(self):
        self.databseHandler.AddRolesInRoleTable()

    def initializeQueues(self):
        self.__queue = Queue()
        self.__deadLetterQueue = Queue()

    def connectToClient(self):
        while True:
            self.createClientSocket()
            self.sendWelcomeMessageToClient()
            self.__clientName = self.serverMessageController.receiveMessageFromClient(
                self.__clientSocket)[DATA]
            print(CONNECTED_TO, self.__clientName)
            start_new_thread(self.startClientThread, ())
        self.serverSocket.close()

    def startClientThread(self):
        try:
            while True:
                self.databseHandler.insertIntoReferenceTable(self.__clientName)
                clientJsonResponse = self.serverMessageController.receiveMessageFromClient(
                    self.__clientSocket)
                if clientJsonResponse[DATA].lower() == TERMINATE:
                    print(self.__clientName+DISCONNECTED)
                    break
                self.handleClientRequest(clientJsonResponse)
            self.__clientSocket.close()
        except:
            raise ClientThreadBrokenException(DEFAULT_EXCEPTION_MESSAGE)

    def handleClientRequest(self, clientJsonResponse):
        if clientJsonResponse[REQUEST_TYPE] == CONNECT:
            topicEnteredByClient = clientJsonResponse[DATA].strip().lower()
            if not self.databseHandler.checkItemNotExistsInTable(topicEnteredByClient, TOPIC):
                self.__topicName = clientJsonResponse[DATA]
                self.serverMessageController.sendMessageToClient(
                    self.__clientSocket, CONNECTION_SUCCESSFULL)
            else:
                self.serverMessageController.sendMessageToClient(
                    self.__clientSocket, TOPIC_UNAVAILABLE)

        if clientJsonResponse[REQUEST_TYPE] == PUBLISH:
            messageToPublish = clientJsonResponse[DATA]
            self.publisherHandler.handlePublishRequest(
                self.__clientSocket, messageToPublish, self.__topicName, self.__queue)
            self.__queue = self.publisherHandler.getUpdatedQueue()

        if clientJsonResponse[REQUEST_TYPE] == SUBSCRIBE:
            self.subscriberHandler.handleSubscribeRequest(
                self.__clientSocket, self.__clientName, self.__topicName,
                self.__queue, self.__deadLetterQueue)

        if clientJsonResponse[REQUEST_TYPE] == ADD:
            self.AddTopicInTopicTable(clientJsonResponse[DATA].lower())

    def AddTopicInTopicTable(self, topicName):
        if self.databseHandler.AddNewTopicInTopicTable(topicName):
            self.serverMessageController.sendMessageToClient(
                self.__clientSocket, NEW_TOPIC_ADDED)
        else:
            self.serverMessageController.sendMessageToClient(
                self.__clientSocket, TOPIC_ALREADY_EXISTS)
