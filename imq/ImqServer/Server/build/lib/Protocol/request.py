from ImqServer.Server.Protocol.imqProtocol import *
from dataclasses import dataclass
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

@dataclass
class Request(ImqProtocol):
    requestType: str = CONNECT
