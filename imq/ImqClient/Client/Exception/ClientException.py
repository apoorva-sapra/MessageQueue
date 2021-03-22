import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('../')
from ExceptionConstants import *

class ClientException(Exception):
    pass

class InvalidCommandException(ClientException):
    pass

class CouldNotConnectToServerException(ClientException):
    pass

class ConnectionBrokenException(ClientException):
    pass

class CommandParserException(ClientException):
    pass

class MessageNotProvidedException(ClientException):
    pass

class DefaultException(ClientException):
    pass