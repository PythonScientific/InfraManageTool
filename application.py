""" Application Class
Base application class for timetable engine.

Author: 	Patryk Zabkiewicz
Date:		2016.03.21

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

from Queue import PriorityQueue
from scheduler import *
from enum import *
from system_info import *


SERVER_STATUSES = enum(INIT=1, RUNNING=2, QUIT=3)
TRUE = 1

class Application(object):
	""" Main class of the application """

	def __init__(self):
		super(Application, self).__init__()
		self.__private_value = 0

		self.start_time = 0					# Start time of the server
		self.running_time = 0				# Uptime of the server
		self.configuration = list() 		# Configuration options container

		self.scheduler = Scheduler() 		# Job scheduler
		self.scheduled_count = 0			# Scheduled task

		self.workers = list() 				# List of workers
		self.worker_count = 10 				# by default 10 workers are avaible

		self.tasks = PriorityQueue() 		# Queue of tasks do be executed
		self.tasks_in_progress = PriorityQueue()	# Tasks currently in progress
		self.tasks_history = Chain()		# Chain of already finished tasks

		self.nodes = list()					# Nodes list of peers
		self.tags = list()					# Tags that are describing the server

		self.current_status = 1				# Current status of the server

		self.SystemInfo = SystemInfo()		# Stores the current system information
		self.ChangeChain = Chain()			# Stores the system status change chain

	def recv_cmd(self):
		""" Recive commands from stdin or other sources """
		cmd = ""
		cmd = raw_input("--->  ")
		return cmd

	def mainloop(self):
		q = TRUE
		self.current_status = SERVER_STATUSES.INIT

		while q:
			cmd = ""
			cmd = self.recv_cmd()
			print cmd

			if (cmd == "quit" or cmd == "exit"):
				q = 0
				print "Quiting..."
			 	pass
		print "Exiting main loop..."
