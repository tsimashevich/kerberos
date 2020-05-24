from des.DES import DES
from models.ticket import Ticket

C_TGS_KEY = 'C_TGSKEY'
AS_TGS_KEY = 'ASTGSKEY'
TGS_ID = 'TGS1'
clientIds = ['userpassword', 'user1password1', 'user2password2']


class AuthenticationService:

    def getAuthTicket(self, clientId):
        des = DES()
        if clientIds.__contains__(clientId):
            tgt = des.encrypt(AS_TGS_KEY, Ticket(clientId, TGS_ID, C_TGS_KEY).getTicket())
            return des.encrypt(clientId, tgt + ',' + C_TGS_KEY)
        else:
            raise Exception('Invalid client id')
