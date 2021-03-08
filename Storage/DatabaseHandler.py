from datetime import datetime
import mysql.connector
from Storage.DatabaseQueries import *
from Storage.DatabaseConstants import * 
from Storage.DatabaseConnectionGenerator import DatabaseConnectionGenerator as db
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class DatabaseHandler:
    databaseConnection = ""
    cursor = ""
    __isTopicDataAdded = True

    def connectWithDatabase(self):
        self.databaseConnection = db.getDatabaseConnection()
        self.cursor = self.getCursor(self.databaseConnection)

    def storeClientRequestInFile(self,clientSocket,fileName,data):
        try:
            with open(fileName, 'a') as file: 
                currentTime=datetime.now().strftime("%H:%M:%S")
                file.write('Client sent '+data + ' at: ' + currentTime +'\n')
        except EOFError as errorMessage:
            print(errorMessage)

    def getCursor(self,databaseConnection):
        cursorObject = databaseConnection.cursor()
        print(cursorObject)
        return cursorObject

    def storeClientRequestInDatabase(self,clientName,data): 
        isTableExists = self.checkClientMessageTableExists()
        if not isTableExists:
            self.createClientMessageTable()
        self.insertDataInClientTable(clientName,data) 

    def checkClientMessageTableExists(self):
        self.cursor.execute(checkClientMessageTableExistsQuery)
        if len(self.cursor.fetchall()) > 0:
            return True
        return False

    def createReferenceTable(self):
        try:
            self.cursor.execute(createReferenceTable)
            self.databaseConnection.commit()
        except:
            print("Reference table could not be created")

    def checkReferenceTableExists(self):
        self.cursor.execute(checkClientMessageTableExistsQuery)
        if len(self.cursor.fetchall()) > 0:
            print("True")
            return True
        return False

    def insertIntoReferenceTable(self,clientName):
        print(self.cursor)
        isTableExists = self.checkReferenceTableExists()
        if not isTableExists:
            self.createReferenceTable()
        value=[clientName]
        print(value)
        self.cursor.execute(checkClientExistsQuery, value)
        isClientExists = self.cursor.fetchall()[0][1]
        if not isClientExists:
            try:
                print("Added in refere table")
                self.cursor.execute(insertQueryForReferenceTable,value)
            except:
                print("Client information could not be stored in reference table")
        self.databaseConnection.commit()

    def createClientMessageTable(self):
        self.cursor.execute(createClientMessageTableCommand)
    
    def getClientId(self, clientName):
        value = [clientName]
        try:
            self.cursor.execute(getClientIdQuery,value)
            clientId = self.cursor.fetchall()[0][0]
            return clientId
        except:
            print("Client id could not be retrieved")
            
    def insertDataInClientTable(self,clientName,data):
        now = datetime.utcnow()
        try:         
            currentTime=now.strftime('%Y-%m-%d %H:%M:%S')
            clientId=self.getClientId(clientName)
            values=(currentTime,data,clientId)
            self.cursor.execute(insertQueryForClientTable,values)
        except:
            print("Client requests could not be saved.")
        self.databaseConnection.commit()
        


