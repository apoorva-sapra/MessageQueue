from dataclasses import dataclass
from Protocol.imqProtocol import *
from Protocol.ProtocolConstants import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

@dataclass
class Response(ImqProtocol):
    status: str = RESPONSE_MESSAGE