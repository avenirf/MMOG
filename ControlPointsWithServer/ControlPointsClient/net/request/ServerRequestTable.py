from common.Constants import Constants

from net.request.RequestMove import RequestMove
from net.request.RequestLogin import RequestLogin
from net.request.RequestHeartbeat import RequestHeartbeat
from net.request.RequestCP import RequestCP

class ServerRequestTable:
    """
    The ServerRequestTable contains a mapping of all requests for use
    with the networking component.
    """
    requestTable = {}

    def __init__(self):
        """Initialize the request table."""
        self.add(Constants.CMSG_AUTH, 'RequestLogin')
        self.add(Constants.CMSG_MOVE, 'RequestMove')
        self.add(Constants.CMSG_CONTROL_POINT_STATE, 'RequestCP')
        self.add(Constants.REQ_HEARTBEAT, 'RequestHeartbeat')

    def add(self, constant, name):
        """Map a numeric request code with the name of an existing request module."""
        if name in globals():
            self.requestTable[constant] = name
        else:
            print 'Add Request Error: No module named ' + str(name)

    def get(self, requestCode):
        """Retrieve an instance of the corresponding request."""
        serverRequest = None

        if requestCode in self.requestTable:
            serverRequest = globals()[self.requestTable[requestCode]]()
        else:
            print 'Bad Request Code: ' + str(requestCode)

        return serverRequest
