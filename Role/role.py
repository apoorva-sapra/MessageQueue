import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from dataclasses import *

@dataclass
class Role:
    roleID = [1,2]
    roleName = ['Publisher', 'Subscriber']
