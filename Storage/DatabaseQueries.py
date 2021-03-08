createReferenceTable ='''CREATE TABLE IF NOT EXISTS ReferenceTable
(
ID INT NOT NULL AUTO_INCREMENT,
clientName VARCHAR(40),
PRIMARY KEY(ID)
)'''
insertQueryForReferenceTable = "INSERT INTO ReferenceTable (ClientName) VALUES (%s)"

createClientMessageTableCommand = '''CREATE TABLE IF NOT EXISTS ClientMessageTable (serialNumber INT AUTO_INCREMENT PRIMARY KEY, timestamp VARCHAR(255), data VARCHAR(255), clientId INT,FOREIGN KEY(clientId) REFERENCES ReferenceTable(ID))'''

checkClientMessageTableExistsQuery = '''SHOW TABLES like "ClientMessageTable"'''

checkReferenceTableExistsQuery = '''SHOW TABLES like "ReferenceTable"'''

checkClientExistsQuery = '''SELECT clientName,COUNT(*) FROM ReferenceTable WHERE clientName = (%s)'''

getClientIdQuery = '''SELECT ID FROM ReferenceTable WHERE ClientName = (%s)'''

insertQueryForClientTable = "INSERT INTO ClientMessageTable (timestamp, data, clientId) VALUES (%s, %s, %s)" 
