import socket
from _thread import start_new_thread 
import sys
import os
sys.path.append('../')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ImqServer.Server.AppConstants import *
from ImqServer.Server.Storage.DatabaseHandler import * 
from ImqServer.Server.ServerMessageController import *
from ImqServer.Server.ServerService import *
from ImqServer.Server.Exceptions.ServerException import *

def startServer():
    host = HOST
    port = PORT
    try:
        server=ServerService()
        server.bindServerSocket(host,port)
        server.startServerListener()
        print(SERVER_AVAILABLE_PROMPT)
        server.createTablesInDatabase()
        server.initializeQueues()
        server.AddTopicsInDatabase()
        server.connectToClient()
    except ServerException as exception:
        print(exception.args[0])
    except Exception as exception:
        print(exception.args[0])

startServer()