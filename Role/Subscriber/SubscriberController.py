import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Role.Subscriber.SubscriberService import *

class SubscriberController:

    def initiateService(self, clientConnection, clientName, topicID):
        subscriberService = SubscriberService(clientConnection, clientName, topicID)
        subscriberService.connectWithDatabase()
        subscriberService.createSubscriberTopicTable()
        subscriberService.createSubscriberMessageMappingTable()
        subscriberService.addDataInSubscriberTopicTable()
        subscriberService.fetchDataFromMessageTable()
        subscriberService.sendMessagesToClient()
