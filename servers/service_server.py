from des.DES import DES

TGS_SS_KEY = 'TGSSSKEY'
SERVER_ID = 'server1'


class ServiceServer:

    def connect(self, encryptedTGS, encryptedAuth):
        des = DES()
        tgs = des.decrypt(TGS_SS_KEY, encryptedTGS).rstrip().split(',')
        auth = des.decrypt(tgs[4], encryptedAuth).rstrip().split(',')
        if tgs[0] == auth[0] and tgs[1] == SERVER_ID and self.checkTimestamp(tgs, auth):
            return des.encrypt(tgs[4], str(float(auth[1]) + 1.0))
        else:
            raise Exception('Wrong TGS')


    def checkTimestamp(self, tgs, auth):
        recvWindow = float(tgs[2])
        tgsTimestamp = float(tgs[3])
        authTimestamp = float(auth[1])
        return tgsTimestamp + recvWindow >= authTimestamp >= tgsTimestamp
