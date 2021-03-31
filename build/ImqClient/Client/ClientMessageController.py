import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ImqClient.Client.Protocol.parser import *
from ImqClient.Client.Protocol.request import *
from ImqClient.Client.AppConstants import *

class ClientMessageController:
    def receiveMessageFromServer(self, clientSocket):
        response = clientSocket.recv(BUFFER).decode('utf-8')
        responseJsonMessage = Parser().JsonDecoder(response)
        return responseJsonMessage

    def sendMessageToServer(self, clientSocket, message, request=CONNECT):
        requestObject = Request(message, HOST, HOST, requestType= request)
        request = Parser().JsonEncoder(requestObject)
        clientSocket.send(str.encode(request))
