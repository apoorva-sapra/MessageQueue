import sys
import os
sys.path.append('../')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

HOST = '127.0.0.1'
PORT = 1233
TERMINATE = "exit"
BUFFER = 1024
WELCOME = "Welcome to the IMQ application"
REQUEST_TYPE = 'requestType'
DATA = 'data'
MESSAGE_PUBLISHED = 'Your message was successfully published'
NEW_TOPIC_ADDED = "New topic Added!"
TOPIC_ALREADY_EXISTS = "Topic already exists!"
TOPIC_UNAVAILABLE = "Topic not available"
CONNECTED_TO = 'Connected to'
DISCONNECTED = " disconnected"
SERVER_AVAILABLE_PROMPT = 'Server waiting for a Connection..'
SAMPLE_COMMAND_FOR_TEST='imq connect sports'
SAMPLE_COMMAND_FOR_GET_CLIENT_ACTION='imq'