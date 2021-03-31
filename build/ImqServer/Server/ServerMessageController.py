import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ImqServer.Server.Protocol.parser import *
from ImqServer.Server.Protocol.response import *
from ImqServer.Server.AppConstants import *

class ServerMessageController:
    def getResponseObject(self, data):
        sourceIp = HOST
        desitantionIP = HOST
        responseObject = Response(data, sourceIp, desitantionIP)
        return responseObject
        
    def sendMessageToClient(self, connection, message):
        responseObject = self.getResponseObject(message)
        responseJsonobject = Parser().JsonEncoder(responseObject)
        connection.sendall(str.encode(responseJsonobject))

    def receiveMessageFromClient(self, connection):
        data = connection.recv(BUFFER)
        response = data.decode('utf-8')
        decodedClientMessage = Parser().JsonDecoder(response)
        return decodedClientMessage