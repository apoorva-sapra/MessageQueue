from dataclasses import dataclass
from imqProtocol import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

@dataclass
class Response(ImqProtocol):
    status: str = "//message sent"