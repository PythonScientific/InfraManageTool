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

import hashlib
import random

class ChainElem(object):
    """ Single chain element """
    def __init__(self, data=[]):
        self.id = 0                 # Element identifier
        self.data = data            # Data storage
        self.next = None              # Refrence to the next element in the chain
        self.prev = None              # Refrence to previous element in the chain
        self.hash = None            # Hash value of next element

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
        """ Returns lenght of chain """
	return self.count

    def hasNext(self):
	""" Returns true if there is next element in chain """
        if self.elem.next:
            return True

    def append(self, elem):
	""" Adds new element to end of chain  """
        # generate new hash
        hashgen = hashlib.sha224(elem.data).hexdigest()
        # put the hash to previous elements
        self.last.hash = hashgen
        self.last.next = elem

    def remove(self, elem):
	""" Removes last element from chain  """
        # remove element from back of the chain
        self.last = self.last.prev
        # remove hash from previous element
        self.last.hash = []

    def insert(self, elem):
	""" Inserts new element at right possition into broken chain """
        # insert element into chain proper position based on hash values
        tmpelem = self.last
        while tmpelem.prev:
            if tmpelem.hash == hashlib.sha224(elem.data).hexdigest():
                elem.next = tmpelem.next
                tmpelem.next = elem
            tmpelem = tmpelem.prev

    def integrity_check(self):
	""" Checks if the chain is compliant """
        # go throu all of chain elements and check integrity
        tmpelem = self.first
        while tmpelem.next:
            if tmpelem.hash != hashlib.sha224(tmpelem.next.data).hexdigest():
                return False
            tmpelem = tmpelem.next
	    return True

if __name__ == "__main__":
    pass
