""" Change class
Stores the information about the change, planned or executed

Author: 	Patryk Zabkiewicz
Date:		2016.03.21

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

class Change(object):
    """ Stores the information about the change, planned or executed """
    def __init__(self, arg):
        super(Change, self).__init__()
        self.arg = arg
