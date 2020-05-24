from datetime import datetime


class Auth:
    clientId = None
    timestamp = None

    def __init__(self, clientId):
        self.clientId = clientId
        self.timestamp = datetime.timestamp(datetime.now())

    def getAuth(self):
        return self.clientId + ',' + str(self.timestamp)
