import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Topic.topicService import *

class TopicController:
    __topicService = ""

    def initializeService(self):
        self.__topicService = TopicService()
        self.__topicService.initilalizeTopic()
        self.__topicService.connectWithDatabase()
    
    def getTopicsList(self):
        topicList = self.__topicService.getTopics()
        return topicList