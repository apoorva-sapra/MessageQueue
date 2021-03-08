from dataclasses import dataclass
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Protocol.imqProtocol import *

@dataclass
class Request(ImqProtocol):
    requestType: str = "connect"
