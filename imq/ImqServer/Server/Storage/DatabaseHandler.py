from datetime import datetime
import mysql.connector
from ImqServer.Server.Storage.DatabaseQueries import *
from ImqServer.Server.Storage.DatabaseConstants import *
from ImqServer.Server.Storage.DatabaseConnectionGenerator import DatabaseConnectionGenerator as db
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class DatabaseHandler:
    databaseConnection = ""
    cursor = ""
    
    def connectWithDatabase(self):
        self.databaseConnection = db.getDatabaseConnection()
        self.cursor = self.getCursor(self.databaseConnection)

    def createDatabaseTables(self):
        self.createReferenceTable()
        self.createTopicTable()
        self.createClientMessageTable()
        self.createRoleTable()
        self.createMessageMappingTable()

    def createReferenceTable(self):
        try:
            self.cursor.execute(createReferenceTable)
            self.databaseConnection.commit()
        except:
            print("Reference table could not be created")

    def createClientMessageTable(self):
        try:
            self.cursor.execute(createClientMessageTableQuery)
            self.databaseConnection.commit()
        except:
            print("Client message table could not be created")

    def createTopicTable(self):
        try:
            self.cursor.execute(createTopicTableQuery)
            self.databaseConnection.commit()
        except:
            print("Topic table could not be created")

    def createRoleTable(self):
        try:
            self.cursor.execute(createRoleTableQuery)
            self.databaseConnection.commit()
        except:
            print("Role table could not be created")

    def createMessageMappingTable(self):
        try:
            self.cursor.execute(createMessageMappingTableQuery)
            self.databaseConnection.commit()
        except:
            print("Message mapping table could not be created")

    def AddTopicsInTopicTable(self):
        values = TOPICS
        for eachTopic in values:
            if self.checkItemNotExistsInTable(eachTopic,TOPIC):
                value = [eachTopic]
                self.cursor.execute(AddTopicInTopicTableQuery,value)
                self.databaseConnection.commit()

    def AddNewTopicInTopicTable(self,topicName):
        if self.checkItemNotExistsInTable(topicName,TOPIC):
            value=[topicName]
            self.cursor.execute(AddTopicInTopicTableQuery,value)
            print(TOPICS)
            self.databaseConnection.commit()
            return True
        return False

    def checkItemNotExistsInTable(self,itemName,table):
        value=[itemName]
        if table == TOPIC:
            self.cursor.execute(checkTopicExistsQuery, value)
        if table == ROLE:
            self.cursor.execute(checkRoleExistsQuery, value)
        isItemExists = self.cursor.fetchall()[0][1]
        if not isItemExists:
            return True
        return False

    def AddRolesInRoleTable(self):
        rolesList = ROLES
        for eachRole in rolesList:
            if self.checkItemNotExistsInTable(eachRole,ROLE):
                value = [eachRole]
                self.cursor.execute(AddRoleInRoleTableQuery,value)
                self.databaseConnection.commit()

    def getCursor(self, databaseConnection):
        cursorObject = databaseConnection.cursor(buffered=True)
        return cursorObject

    def storeClientRequestInDatabase(self, clientName, data):
        isTableExists = self.checkClientMessageTableExists()
        if not isTableExists:
            self.createClientMessageTable()
        self.insertDataInClientMessageTable(clientName, data)

    def checkClientMessageTableExists(self):
        self.cursor.execute(checkClientMessageTableExistsQuery)
        if len(self.cursor.fetchall()) > 0:
            return True
        return False

    def checkReferenceTableExists(self):
        self.cursor.execute(checkClientMessageTableExistsQuery)
        if len(self.cursor.fetchall()) > 0:
            return True
        return False

    def insertIntoReferenceTable(self, clientName):
        self.connectWithDatabase()
        isTableExists = self.checkReferenceTableExists()
        if not isTableExists:
            self.createReferenceTable()
        value = [clientName]
        self.cursor.execute(checkClientExistsQuery, value)
        isClientExists = self.cursor.fetchall()[0][1]
        if not isClientExists:
            try:
                self.cursor.execute(insertQueryForReferenceTable, value)
            except:
                print("Client information could not be stored in reference table")
        self.databaseConnection.commit()

    def getClientId(self, clientName):
        value = [clientName]
        try:
            self.cursor.execute(getClientIdQuery, value)
            clientId = self.cursor.fetchall()[0][0]
            return clientId
        except:
            print("Client id could not be retrieved")

    def getTopicId(self, topicName):
            topicName=topicName.strip()
            value = [topicName]
            # try:
            self.cursor.execute(getTopicIdQuery, value)
            topicId = self.cursor.fetchall()[0][0]
            return topicId
            # except:
            #     print("Topic id could not be retrieved")       

    def insertDataInClientMessageTable(self,data,topicName):
        now = datetime.utcnow()
        try:
            currentTime = now.strftime('%Y-%m-%d %H:%M:%S')
            topicId=self.getTopicId(topicName)
            values = (currentTime, data, topicId)
            self.cursor.execute(insertQueryForClientMessageTable, values)
            print("Published 1 message.")
        except:
            print("Client message could not be published.")
        self.databaseConnection.commit()

    def checkClientAndTopicExistInMessageMapping(self,clientId,topicId):
        values=(clientId,topicId)
        self.cursor.execute(checkClientAndTopicExistInMessageMappingQuery,values)
        isClientExists = self.cursor.fetchall()[0][1]
        return isClientExists

    def getMessagesFromClientMessageTable(self, topicId):
        value = [topicId]
        self.cursor.execute(getMessagesFromClientMessageTableQuery,value)
        messages = self.cursor.fetchall()
        return messages

    def addDataInMessageMappingTable(self, clientId, topicId, lastSeenMessageId):
        value =[clientId,topicId,lastSeenMessageId]
        self.cursor.execute(addDataInMessageMappingTableQuery,value)
        self.databaseConnection.commit()

    def getLastSeenMessageIdFromMessageMappingTable(self,topicId, clientId):
        value = [topicId, clientId]
        self.cursor.execute(getLastSeenMessageIdFromMessageMappingTableQuery, value)
        lastSeenMessageId = self.cursor.fetchall()[0][0]
        return lastSeenMessageId
        
    def getUnseenMessagesFromDatabase(self,lastSeenMessageId,topicId):
        value=[topicId,lastSeenMessageId]
        self.cursor.execute(getUnseenMessagesQuery,value)
        messages = self.cursor.fetchall()
        return messages

    def updateLastSeenMessageId(self,lastSeenMessageId,clientId,topicId):
        value=[lastSeenMessageId,clientId,topicId]
        self.cursor.execute(updateLastSeenMessageIdQuery,value)
        self.databaseConnection.commit()
        
    def getLastMessageId(self):
        return self.cursor.lastrowid