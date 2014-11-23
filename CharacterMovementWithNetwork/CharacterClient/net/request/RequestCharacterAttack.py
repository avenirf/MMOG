from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestCharacterAttack(ServerRequest):


    def send(self, args = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CSMG_ATTACK)
            pkg.addInt32(args)#attackid

            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_INT) + '] Int Request')
        except:
            self.log('Bad [' + str(Constants.RAND_INT) + '] Int Request')
            print_exc()