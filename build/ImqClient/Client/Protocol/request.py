from Protocol.imqProtocol import *
<<<<<<< HEAD
from Protocol.ProtocolConstants import *
=======
>>>>>>> ff40b13149e9dadd0ec290899024c6c2d83e761a
from dataclasses import dataclass
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

@dataclass
class Request(ImqProtocol):
    requestType: str = CONNECT
