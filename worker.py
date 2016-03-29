""" Worker Class
Worker is the process that controls execution of tasks

Author: 	Patryk Zabkiewicz
Date:		2016.03.21

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

from Thread import Thread

class Worker:
	""" Worker is the process that controls execution of tasks """
	def __init__(self):
		self.ttl = 5
		self.ttl_thread = Thread()
		pass

	def setup_work(self, work_struct):
		""" This method sets up a task for worker by reciving work structure """
		pass

	def recv_ping(self):
		self.ttl = 5
		pass

	def do_work(self):
		""" This is the main task executor """
		pass
