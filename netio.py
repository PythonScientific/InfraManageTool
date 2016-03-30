
from queue import Queue
from msg import MSG


class NetIO(object):
    """ NetIO is reponsible for communication with other peers """
    def __init__(self, arg):
        super(NetIO, self).__init__()
        self.in_buffer = Queue()        # buffer for input
        self.out_buffer = Queue()       # buffer for output
        self.peers = list()             # List of peers

    def send(self):
        """ single messange send to all peers """
        pass

    def recv(self):
        """ single messange recv from peers """
        for p in self.peers:
            self.in_buffer.put(p.recv())

    def buffer_read(self):
        """ read next messange from recive buffer """
        return self.in_buffer.get()

    def buffer_send(self):
        """ write next messange to send buffer """
        pass
