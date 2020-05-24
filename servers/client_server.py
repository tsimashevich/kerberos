from des.DES import DES
from kerberous.authentication_service import AuthenticationService
from kerberous.ticket_granting_server import TicketGrantingServer
from models.auth import Auth
from servers.service_server import ServiceServer


class ClientServer:
    clientId = None
    serverId = 'server1'
    authTicket = None
    grantingTicket = None

    def __init__(self, clientId):
        self.clientId = clientId

    def authenticate(self):
        des = DES()
        authService = AuthenticationService()
        self.authTicket = des.decrypt(self.clientId, authService.getAuthTicket(self.clientId)).rstrip().split(',')


    def getGrantingTicket(self):
        des = DES()
        tgs = TicketGrantingServer()
        auth = Auth(self.clientId)
        grantingTicket = tgs.getGrantingTicket(self.authTicket[0], des.encrypt(self.authTicket[1], auth.getAuth()), self.serverId)
        self.grantingTicket = des.decrypt(self.authTicket[1], grantingTicket).rstrip().split(',')


    def connectToServer(self):
        des = DES()
        server = ServiceServer()
        auth = Auth(self.clientId)
        serverResponse = server.connect(self.grantingTicket[0], des.encrypt(self.grantingTicket[1], auth.getAuth()))
        timestamp = float(des.decrypt(self.grantingTicket[1], serverResponse).rstrip())
        if timestamp == float(auth.timestamp) + 1.0:
            print('Success')
