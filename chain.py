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
        self.data = data            # Data storage
        self.next = None              # Refrence to the next element in the chain
        self.prev = None              # Refrence to previous element in the chain
        self.prev3 = None             # Refrence to (n-3) element
        self.prev5 = None             # Refrence to (n-5) element
        # Hash values are use for data integrity checks
        # Hooks are attached to the previous values in Fibonnaci fashion
        self.prevhash1 = None         # Hash value with previous (n-1) element in the chain
        self.prevhash3 = None         # Hash value with (n-3) element in the chain
        self.prevhash5 = None         # Hash value with (n-5) element in the chain
        self.nexthash = None          # Hash value of next element

class Chain(object):
    """ The chain structure for data (iterable) """
    def __init__(self):
        super(Chain, self).__init__()
        self.elem = None              # Element of chain with data
        self.first = None             # Refrence to first element
        self.last = None              # Refrence to last element
        self.count = 0              # Count of elements in chain
        self.max = 0                  # Maximum number of elements

    def lenght():
        return self.count

    def hasNext(self):
        if self.elem.next:
            return True

    def append(self, elem):
        # generate new hash
        # put the hash to previous elements
        pass

    def remove(self, elem):
        # remove element from back of the chain
        # remove hash from previous element
        pass

    def insert(self, elem):
        # insert element into chain proper position based on hash values
        pass

    def integrity_check(self):
        # go throu all of chain elements and check integrity
        pass

if __name__ == "__main__":
    pass
