import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from dataclasses import dataclass
from ImqServer.Server.Protocol.ProtocolConstants import *

@dataclass
class ImqProtocol:
    data: str
    sourceUrl: str
    desitantionUrl: str
    dataformat: str = FORMAT
    version: str = VERSION
