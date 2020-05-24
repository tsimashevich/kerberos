from datetime import datetime


class Ticket:
    recvWindow = '60'  # период действия билета в секндах.
    serverId = None    # идентификатор сервера
    clientId = None    # идентификатор клиента
    timestamp = None   # время создания билета
    key = None         # ключ для доступа к серверу

    def __init__(self, clientId, serverId, tgsKey):
        self.clientId = clientId
        self.tgsKey = tgsKey
        self.serverId = serverId
        self.timestamp = str(datetime.timestamp(datetime.now()))

    def getTicket(self):
        return self.clientId + ',' + self.serverId + ',' + self.recvWindow + ',' + self.timestamp + ',' + self.tgsKey
