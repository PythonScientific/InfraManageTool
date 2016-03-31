
class Peer(object):
    """ Implementation of the network peer """
    def __init__(self):
        super(Peer, self).__init__()
        self.out_buffer = Queue()       # buffer to send out messanges
        self.in_buffer = Queue()        # buffer to recv messanges from peer
        self.address = []
        self.connection = []
        pass

    def send(self):
        """ Send out single messange to other peer """
        # connect to peer
        # handshake
        # send out messange
        # close connection
        pass
