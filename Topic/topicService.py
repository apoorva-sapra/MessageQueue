import sys
import os
sys.path.append('../')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Storage.DatabaseHandler import *

class TopicService: 
    __listOfTopics = []

    def initilalizeTopic(self):
        self.__listOfTopics = [('Morning Updates',),('Evening Updates',)]

    def getTopics(self):
        return self.__listOfTopics

    def connectWithDatabase(self):
        databaseController = DatabaseHandler()
        databaseController.initDatabaseConnection() 
        self.__addTopicsInDatabase(databaseController)

    def __addTopicsInDatabase(self, databaseController): 
        databaseController.createTopicTable()
        databaseController.addTopicDataIntoTable(self.__listOfTopics)
