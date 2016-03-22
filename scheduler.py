""" Scheduler Class
Base application class for timetable engine.

Author: 	Patryk Zabkiewicz
Date:		2016.03.22

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

from Queue import Queue
from task import *

class Scheduler:
	def __init__(self):
		self.__private = 0
		self.scheduled_tasks = Queue() # list of scheduled tasks

	def schedule_change(self, change_struct):
		""" Adds new record to priority queue list """
		pass
