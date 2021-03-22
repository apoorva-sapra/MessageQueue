import sys
import os
sys.path.append('../')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
import socket
from ImqServer.Server.AppConstants import *
from ImqServer.Server.ServerMessageController import *
from ImqServer.Server.ServerService import *

class Server_Test(unittest.TestCase):
    serverObject = ServerService()
    serverSocket = socket.socket()
    serverMessageControllerObject=ServerMessageController()

    def testSocketCreation(self):
        socketCreated = self.serverObject.createServerSocket()
        self.assertEqual(type(socketCreated), type(self.serverSocket))
        socketCreated.close()

    def testSocketBinding(self):
        self.assertIsNone(self.serverObject.bindServerSocket(HOST,PORT))

    def testSocketIsListening(self):
        self.assertIsNone(self.serverObject.startServerListener())

    def testAllTablesCreatedInDatabase(self):
        self.assertIsNone(self.serverObject.createTablesInDatabase())
        
    def testInitiationOfMessageQueues(self):
        self.assertIsNone(self.serverObject.initializeQueues())
    