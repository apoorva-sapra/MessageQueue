import socket
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('../')
from Client.AppConstants import *
from Client.ClientMessageController import *
from Client.ClientService import *
from Client.Exception.ClientException import *

def startClient():
    try:   
        client=ClientService()
        client.connectClientToServer()
        client.getWelcomeMessageFromServer()
        client.communicateWithServer()
    except ClientException as exception:
        print(exception.args[0])

startClient()
