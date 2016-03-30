
class Peer(object):
    """ Implementation of the network peer """
    def __init__(self):
        super(Peer, self).__init__()
        self.out_buffer = Queue()       # buffer to send out messanges
        self.in_buffer = Queue()        # buffer to recv messanges from peer
        pass

    def send():
        pass
