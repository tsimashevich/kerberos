from des.DES import DES
from models.ticket import Ticket

AS_TGS_KEY = 'ASTGSKEY'
C_SS_KEY = 'C_SS_KEY'
TGS_SS_KEY = 'TGSSSKEY'
TGS_ID = 'TGS1'
serverIds = ['server1', 'server2', 'server3']


class TicketGrantingServer:

    def getGrantingTicket(self, encryptedTGT, encryptedAuth, serverId):
        des = DES()
        tgt = des.decrypt(AS_TGS_KEY, encryptedTGT).rstrip().split(',')
        auth = des.decrypt(tgt[4], encryptedAuth).rstrip().split(',')
        if tgt[0] == auth[0] and tgt[1] == TGS_ID and self.checkTimestamp(tgt, auth) and serverIds.__contains__(serverId):
            tgs = des.encrypt(TGS_SS_KEY, Ticket(tgt[0], serverId, C_SS_KEY).getTicket())
            return des.encrypt(tgt[4], tgs + ',' + C_SS_KEY)
        else:
            raise Exception('Wrong TGT')


    def checkTimestamp(self, tgt, auth):
        recvWindow = float(tgt[2])
        tgtTimestamp = float(tgt[3])
        authTimestamp = float(auth[1])
        return tgtTimestamp + recvWindow >= authTimestamp >= tgtTimestamp

