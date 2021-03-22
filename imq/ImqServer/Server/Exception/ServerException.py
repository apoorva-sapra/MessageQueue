import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('../')
from ExceptionConstants import *

class ServerException(Exception):
    pass

class SocketException(ServerException):
    pass

class ClientThreadBrokenException(ServerException):
    pass

class ServerListenerException(ServerException):
    pass

class ServerAcceptorException(ServerException):
    pass

class MessageNotProvidedException(ServerException):
    pass
