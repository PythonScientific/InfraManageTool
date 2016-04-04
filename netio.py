""" NetIO
Reponsible for communication with other peers

Main idea is about:
    - sendout asynchronus messanges to another peers
    - process one messange from queue to all peers
    -

Author: Patryk Zabkiewicz
Date:	2016.03.30

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

from Queue import Queue
from msg import MSG
from semaphore_queue import *

def init():
    pass

class NetIO(object):
    """ NetIO is reponsible for communication with other peers """
    def __init__(self, arg):
        super(NetIO, self).__init__()
        self.in_buffer = SemaphoreQueue()       # buffer for input
        self.out_buffer = SemaphoreQueue()      # buffer for output
        self.peers = list()                     # List of peers

    def send(self):
        """ single messange send to all peers """
        msg = self.out_buffer.get()
        for p in self.peers: # go throu all peers
            p.out_buffer.put(msg)

    def recv(self):
        """ single messange recv from other peers """
        for p in self.peers: # go throu all peers
            self.in_buffer.put(p.recv())

    def buffer_read(self):
        """ read next messange from recive buffer """
        return self.in_buffer.get()

    def buffer_send(self, msg):
        """ write next messange to send buffer """
        self.out_buffer.put(msg)

if __name__ == "__main__":
    pass
