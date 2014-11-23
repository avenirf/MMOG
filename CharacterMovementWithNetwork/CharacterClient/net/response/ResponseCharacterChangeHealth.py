from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCharacterChangeHealth(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            self.healthChange = data.getInt32()

            #actions
            if self.main.player.get_name == self.username:
                        self.main.player.set_health(self.main.player.get_health - self.healthChange)
            else:
                        self.main.characters[username].set_health(self.main.characters[username].get_health + self.healthChange)
        except:
            self.log('Bad [' + str(Constants.SMGS_ATTACK) + '] Attack Response')
            print_exc()
