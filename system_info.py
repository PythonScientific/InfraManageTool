""" SystemInfo class
Stores the current system status

Author: 	Patryk Zabkiewicz
Date:		2016.03.29

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

class SystemInfo(object):
    """ Stores the current system status """
    def __init__(self, arg):
        super(SystemInfo, self).__init__()
        self.arg = arg
        self.infomation = list()

    def apply_change(self,change):
        pass
