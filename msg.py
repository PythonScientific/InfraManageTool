""" MSG class
Basic structure for messanges between peers

Author: Patryk Zabkiewicz
Date:	2016.03.30

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

class MSG:
    """ Basic structure for messanges between peers """
    id = 0                          # id of the messanges / static member

    def __init__(self):
        self.timestamp = []         # timestamp
        self.data = []              # data to be sended out
        self.sumbit = 0             # CRC sum bit
        self.bitout = []            # encoded bits to send out throu network

    def calculateCRC(self):
        """ Calculates CRC sum and fills out sum bit """
        pass

    def encode(self):
        """ Encode the bit out of the messange """
        pass

    def decode(self):
        """ Decode the bit out of the messange """
        pass

    @staticmethod
    def getID():
        MSG.id += 1
        return MSG.id

if __name__ == "__main__":
    pass
