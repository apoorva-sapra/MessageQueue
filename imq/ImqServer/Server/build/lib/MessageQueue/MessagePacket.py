class MessagePacket:

    def __init__(self, topicName, message, messageArrivalTime):
        self.messageId = 1
        self.topicName = topicName
        self.data = message
        self.arrivalTime = messageArrivalTime