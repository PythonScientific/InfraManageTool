""" Logger class
Logger controls the application logging capabilites

Author: Patryk Zabkiewicz
Date:	2016.03.21

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

from enum import *

LOG_LEVEL = enum(INFO=1, WARRNING=2, ERROR=3)

class LogLine(object):
    """ One line of logs """
    def __init__(self, arg):
        super(LogLine, self).__init__()
        self.level = LOG_LEVEL
        self.messange = ""

class Logger(object):
    """ Logger controls the application logging capabilites """
    def __init__(self):
        super(Logger, self).__init__()
	self.log_store = "~/.timetable"		# Standard log path
	self.log_buffer_size = 10		# Default log buffer size to disk store
	self.log_buffer_count = 0		# Count of the messanges in the buffer
	self.log_buffer = list()		# Log buffer
        self._logfile = ""                  	# Path to logfile
        self._logfilename = ""              	# Log file name

    def log(self, messange):
	self.log_buffer.append(messange)
	self.log_buffer_count += 1

if __name__ == "__main__":
    pass
