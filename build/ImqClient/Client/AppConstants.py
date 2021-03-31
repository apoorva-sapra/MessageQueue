import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('../')
HOST = '127.0.0.1'
PORT = 1233
TERMINATE = "exit"
BUFFER = 1024
HELP_STRING = "-----------IMQ COMMANDS MANUAL----------- \n   imq connect topic_name \n   imq add topic_name\n   imq publish -m \"your_message\" \n   imq subscribe \n   imq manual \n   exit"
IMQ = 'imq'
CONNECT = 'connect'
PUBLISH = 'publish'
SUBSCRIBE = 'subscribe'
ADD = 'add'
INVALID_COMMAND = "\tInvalid command \n\timq manual for manual"
MANUAL = "manual"
CLIENT_ACTIONS = ['connect', 'publish', 'subscribe', 'add', 'manual']
DATA = 'data'
ENTER_USERNAME_STRING = "Please provide your unique username to connect. \n"
SERVER_CONNECTED = "Connected to server"
COMMAND = ">>> "
PULL = 'pull'
FIRST_CONNECT_TO_TOPIC_MESSAGE = "Please connect to topic before publishing or subscribing."
SAMPLE_TOPIC = 'sports'
SAMPLE_COMMAND_FOR_TEST = 'imq connect sports'
SAMPLE_COMMAND_FOR_IMPLEMENTATION_TEST = 'imq manual'
