import socket
import unittest
import sys
import os
sys.path.append('../')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ImqClient.Client.ClientService import *
from ImqClient.Client.AppConstants import *
from ImqClient.Client.Exception.ClientException import *

class Client_Test(unittest.TestCase):
    clientObject = ClientService()
    clientSocket = socket.socket()

    def testRecieveMessageFrom(self):
        self.assertIsNone(self.clientObject.displayHelpString())

    def testImplementClientAction(self):
        self.assertIsNone(self.clientObject.implementClientAction(
            SAMPLE_COMMAND_FOR_IMPLEMENTATION_TEST))

    def testImplementConnectAction(self):
        self.assertRaises(CommandParserException)

    def testGetTopc(self):
        clientAction = self.clientObject.getClientAction(
            SAMPLE_COMMAND_FOR_TEST)
        self.assertEqual(clientAction, CONNECT)

    def testGetClientAction(self):
        topic = self.clientObject.getTopic(SAMPLE_COMMAND_FOR_TEST)
        self.assertEqual(topic, SAMPLE_TOPIC)
