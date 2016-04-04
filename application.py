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
from chain import *
from main import version,help
from logger import *
from manual import *
import alerts

SERVER_STATUSES = enum(INIT=1, RUNNING=2, QUIT=3)
TRUE = 1

class Application(object):
	""" Main class of the application """

	def __init__(self):
		super(Application, self).__init__()
		self.__private_value = 0

		self.logger = Logger()				# Logger

		self.alerts = list()				# Customizable alerts for events
		self.alerts_count = 0				# Count of created alerts

		self.start_time = 0					# Start time of the server
		self.running_time = 0				# Uptime of the server

		self.config_file_path = ""			# Configuration file path
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
		self.system_info = list()			# Stores the current system information

	def recv_cmd(self):
		""" Recive commands from stdin or other sources """
		cmd = ""
		cmd = raw_input("--->  ")
		return cmd

	def initate(self):
		""" This initializes the application specific items """

		# logger start
		self.logger.log("")

		# init configuration
		self.configuration.append("")

		# init

		# init alerts
		# read from saved state and add to list
		alerts.init()

		pass

	def mainloop(self):
		""" Recive a command from stdin CLI and send it out to application engine """
		q = TRUE
		self.current_status = SERVER_STATUSES.INIT

		while q:
			cmd = ""
			cmd = self.recv_cmd()
			if (cmd == "quit" or cmd == "exit"):
				q = 0
				print "Quiting..."
			if cmd == "help":
				version()
				help()
			if cmd == "list":
				list_help()
			if cmd == "get":
				get_help()
			if cmd == "get peers":
				print "getting peers..."
			if cmd == "list peers":
				print "listing peers..."
			if cmd == "commit":
				print "commiting changes..."
			if len(cmd) > 0:
				print "unknown command"

		print "Exiting main loop..."

if __name__ == "__main__":
    pass
