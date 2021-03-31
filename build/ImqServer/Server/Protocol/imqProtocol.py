<<<<<<< HEAD
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from dataclasses import dataclass
from ImqServer.Server.Protocol.ProtocolConstants import *
=======
from dataclasses import dataclass
from Protocol.ProrocolConstants import *
>>>>>>> ff40b13149e9dadd0ec290899024c6c2d83e761a

@dataclass
class ImqProtocol:
    data: str
    sourceUrl: str
    desitantionUrl: str
    dataformat: str = FORMAT
    version: str = VERSION
