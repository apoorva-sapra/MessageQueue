import json
import jsonpickle
from json import JSONEncoder
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class Parser:

    def JsonEncoder(self, requestObject):
        imqJson = jsonpickle.encode(requestObject, unpicklable=False)
        return json.dumps(imqJson, indent=4)

    def JsonDecoder(self, responseObject):
        imqJson = jsonpickle.decode(responseObject)
        return json.loads(imqJson)