""" Chain class
The chain structure for data

Chain differs from other types like list or queue because the elements comes
in specified order and the order of chain cannot be changed. Structure controls
integrity of data and auto-repairs itself.

Author: Patryk Zabkiewicz
Date:	2016.03.21

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

class ChainElem(object):
    """ Single chain element """
    def __init__(self, data):
        self.data = data
        self.next = []
        self.prev = []
        self.hash = []
        pass

class Chain(object):
    """ The chain structure for data (iterable) """
    def __init__(self):
        super(Chain, self).__init__()
        self.elem = []
        self.first = []
        self.last = []
        self.count = 0
        pass

    def lenght():
        return len(data)

    def hasNext(self):
        if self.next
            return True

    def append(self, elem):
        # generate new hash
        # put the hash to previous element
        pass

    def remove(self, elem):
        # remove element from back of the chain
        # remove hash from previous element
        pass
