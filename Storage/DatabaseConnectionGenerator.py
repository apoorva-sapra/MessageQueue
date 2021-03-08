import mysql.connector
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Storage.DatabaseConstants import *

class DatabaseConnectionGenerator:
    databaseConnection = None

    @staticmethod
    def getDatabaseConnection():
        if DatabaseConnectionGenerator.databaseConnection == None:
            DatabaseConnectionGenerator()
        return DatabaseConnectionGenerator.databaseConnection

    def __init__(self):
        if DatabaseConnectionGenerator.databaseConnection != None:
            raise Exception("Database already connected!")
        else:
            databaseConnection = mysql.connector.connect(
                host=DATABASE_HOST,
                user=DATABASE_USER,
                password=DATABASE_PASSWORD,
                database=DATABASE
            )
            DatabaseConnectionGenerator.databaseConnection = databaseConnection


