from datetime import datetime, timedelta
import sys
import os
sys.path.append('../')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class QueueHandler:
    __queueObject = ""
    __deadLetterQueue = ""

    def handleMessageQueue(self, queue, deadLetterQueue):
        self.__queueObject = queue
        self.__deadLetterQueue = deadLetterQueue
        self.removeExpiredMessagesFromQueue()

    def removeExpiredMessagesFromQueue(self):
        expiryTime = datetime.now() - timedelta(minutes=10)
        for eachMessagePacket in self.__queueObject.queue:
            if eachMessagePacket.arrivalTime < expiryTime:
                self.addExpiredMessagesToDeadLetterQueue(eachMessagePacket)
                self.__queueObject.queue.remove(eachMessagePacket)

    def addExpiredMessagesToDeadLetterQueue(self, messagePacket):
        self.__deadLetterQueue.queue.append(messagePacket)
        print(len(self.__deadLetterQueue.queue))
