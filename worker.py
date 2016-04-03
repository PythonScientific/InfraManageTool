""" Worker Class
Worker is the process that controls execution of tasks

Author: 	Patryk Zabkiewicz
Date:		2016.03.21

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

from Thread import Thread
from Queue import Queue

TTL = 5

class Worker(object):
	""" Worker is the process that controls execution of tasks """
	def __init__(self,task_list):
		self.ttl = 5
		self.ttl_thread = Thread()
		self.task_list = task_list
		self.task_queue = Queue() # Queue of task to execute
		pass

	def setup_work(self, work_struct):
		""" This method sets up a task for worker by reciving work structure """
		pass

	def recv_ping(self):
		""" By reciving ping sets up the ttl back to original value """
		self.ttl = TTL

	def ping(self):
		""" Send out ping to say I am alive and well """
		self.recv_ping()

	def do_work(self):
		""" This is the main task executor """
		pass
