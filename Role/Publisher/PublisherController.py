import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Role.Publisher.PublisherService import *

class PublisherController:

    def initiateService(self, clientSocket, clientName, topicID):
        publisherService = PublisherService(clientSocket, clientName, topicID)
        publisherService.connectWithDatabase()
        publisherService.createPublisherTopicTable()
        publisherService.addDataInTable()
        publisherService.publishDataInTable()