import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('../')

SOCKET_EXCEPTION_MESSAGE='Socket could not be created'
DEFAULT_EXCEPTION_MESSAGE= "Something went wrong"
SERVER_LISTENER_EXCEPTION_MESSAGE="Server not listening for clients."
SERVER_ACCEPTOR_EXCEPTION_MESSAGE="Server not able to accept clients"