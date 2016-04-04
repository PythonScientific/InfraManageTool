""" Alerts Class
Alerts signals the non acceptable state of the system

Author: 	Patryk Zabkiewicz
Date:		2016.03.21

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

import os.path

FNAME = ".imt/stored-alerts"

def init():
    # read all allerts from saved state
    if os.path.isfile(FNAME):
        with open(FNAME) as f:
            content = f.readlines()
        # create and return the list of allerts
        lst_allerts = list()
        for x in content:
            lst_allerts.append(Alert())
        return lst_allerts
    else:
        # if no file with alerts than return empty list
        return list()

class Alert(object):
    """ Alerts signals the non acceptable state of the system """
    def __init__(self):
        super(Alert, self).__init__()
        self.active = 0			# Is the alarm active now?
        self.ttl = 0			# Time to alarm goes of since last ping to it
        self.time_schedule = list()	# List of scheduled times for alarm to goes off
        self.event = list()		# List of events when alarm goes off

    def activate(self):
	self.active = 1

    def deactivate(self):
	self.active = 0

if __name__ == "__main__":
    pass
