""" UCI class
Communication interface abstraction class
No matter from where the new commands come from they will be interpreted
by this absract interface

Author: Patryk Zabkiewicz
Date:	2016.04.04

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

class UCI(object):
    """docstring for UCI"""
    def __init__(self):
        super(UCI, self).__init__()
        self.data = []
