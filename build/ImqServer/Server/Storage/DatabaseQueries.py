createReferenceTable = '''
CREATE TABLE IF NOT EXISTS ReferenceTable
(
clientId INT NOT NULL AUTO_INCREMENT,
clientName VARCHAR(40),
PRIMARY KEY(clientId)
);'''

createClientMessageTableQuery = '''CREATE TABLE IF NOT EXISTS ClientMessageTable 
(messageId INT AUTO_INCREMENT PRIMARY KEY, 
arrivalTime VARCHAR(255), 
data VARCHAR(255), 
topicId INT,
FOREIGN KEY(topicId) REFERENCES topic(topicId));'''

createTopicTableQuery = '''CREATE TABLE IF NOT EXISTS TOPIC
(
topicId INT NOT NULL AUTO_INCREMENT,
topicName VARCHAR(40),
PRIMARY KEY(topicId)
);'''

createRoleTableQuery = '''CREATE TABLE IF NOT EXISTS ROLE
(
roleId INT NOT NULL AUTO_INCREMENT,
roleName VARCHAR(20),
PRIMARY KEY(roleId)
);'''

createMessageMappingTableQuery = '''CREATE TABLE IF NOT EXISTS MESSAGEMAPPINGTABLE
(
clientId INT NOT NULL,
topicId INT NOT NULL,
lastSeenMessageId INT NOT NULL,
FOREIGN KEY(lastSeenMessageId) REFERENCES clientmessagetable(messageId),
FOREIGN KEY(clientId) REFERENCES referencetable(clientId),
FOREIGN KEY(topicId) REFERENCES topic(topicId)
);'''

AddTopicInTopicTableQuery = '''INSERT INTO TOPIC (topicName) VALUES (%s)'''

AddRoleInRoleTableQuery = '''INSERT INTO ROLE (roleName) VALUES (%s)'''

insertQueryForReferenceTable = "INSERT INTO ReferenceTable (clientName) VALUES (%s)"

checkClientMessageTableExistsQuery = '''SHOW TABLES like "ClientMessageTable"'''

checkReferenceTableExistsQuery = '''SHOW TABLES like "ReferenceTable"'''

checkClientExistsQuery = '''SELECT clientName,COUNT(*) FROM ReferenceTable WHERE clientName = (%s)'''

checkTopicExistsQuery = '''SELECT topicName,COUNT(*) FROM topic WHERE topicName = (%s)'''

checkRoleExistsQuery = '''SELECT roleName,COUNT(*) FROM role WHERE roleNAme = (%s)'''

getClientIdQuery = '''SELECT clientId FROM REFERENCETABLE WHERE ClientName = (%s)'''

getTopicIdQuery = '''SELECT topicId FROM TOPIC WHERE topicName = (%s)'''

insertQueryForClientMessageTable = "INSERT INTO ClientMessageTable (arrivalTime, data, topicId) VALUES (%s, %s, %s)"

dropTopicTableQuery = '''DROP TABLE IF EXISTS topic'''

checkClientAndTopicExistInMessageMappingQuery = '''SELECT clientId, count(*) from MESSAGEMAPPINGTABLE WHERE clientId = (%s) AND topicId = (%s)'''

getUnseenMessagesQuery = "SELECT data, messageId FROM CLIENTMESSAGETABLE WHERE topicId = (%s) AND messageId > (%s)"

getMessagesFromClientMessageTableQuery = "SELECT data, messageId FROM CLIENTMESSAGETABLE WHERE topicId = %s"

addDataInMessageMappingTableQuery = '''INSERT INTO MESSAGEMAPPINGTABLE (clientId, topicId, lastSeenMessageId) VALUES(%s,%s,%s)'''

getLastSeenMessageIdFromMessageMappingTableQuery = "SELECT lastSeenMessageId FROM MESSAGEMAPPINGTABLE WHERE topicId = (%s) AND clientId = (%s)"

updateLastSeenMessageIdQuery = '''UPDATE MESSAGEMAPPINGTABLE SET lastSeenMessageId = (%s) WHERE clientId = (%s) AND topicId = (%s)'''
