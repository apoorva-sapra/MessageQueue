import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Protocol.parser import *
from Protocol.request import *
from Client.AppConstants import *

class ClientController:
    def receiveMessageFromServer(self, clientSocket):
        response = clientSocket.recv(BUFFER).decode('utf-8')
        responseJsonMessage = Parser().JsonDecoder(response)
        return responseJsonMessage

    def sendMessageToServer(self, clientSocket, message):
        requestObject = Request(message, HOST, HOST)
        request = Parser().JsonEncoder(requestObject)
        clientSocket.send(str.encode(request))
