from dataclasses import dataclass

@dataclass
class ImqProtocol:
    data: str
    sourceUrl: str
    desitantionUrl: str
    dataformat: str = "json"
    version: str = "1.0"
