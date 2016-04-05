""" Application Class
Base application class for timetable engine.

Author: 	Patryk Zabkiewicz
Date:		2016.03.21

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

from Queue import PriorityQueue
from enum import *
from chain import *
from main import version,help,VERSION
from manual import *

import logger
import alerts
import netio
import configuration
import scheduler
import worker

SERVER_STATUSES = enum(INIT=1, RUNNING=2, QUIT=3)
TRUE = 1

class Application(object):
	""" Main class of the application """

	def __init__(self):
		super(Application, self).__init__()
		self.__private_value = 0

		self.logger = []					# Logger

		self.alerts = list()				# Customizable alerts for events
		self.alerts_count = 0				# Count of created alerts

		self.start_time = 0					# Start time of the server
		self.running_time = 0				# Uptime of the server

		self.config_file_path = ""			# Configuration file path
		self.configuration = list() 		# Configuration options container

		self.scheduler = scheduler.Scheduler() 		# Job scheduler
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

		self.networking = []				# networking IO interface
		self.uci = []						# unified communication interface

	def recv_cmd(self):
		""" Recive commands from stdin or other sources """
		cmd = ""
		cmd = raw_input("--->  ")
		return cmd

	def init(self):
		""" This initializes the application specific items """
		# logger start
		self.logger = logger.Logger()
		self.logger.log(" *** Starting the engine *** ")
		self.logger.log(VERSION)
		# init configuration
		self.configuration = configuration.init()
		# init scheduler
		self.scheduler = scheduler.init()
		# init networking
		self.networking = netio.init()
		# init worker threads
		self.threads = worker.init()
		# init alerts
		self.alerts = alerts.init()

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
				continue
			if cmd == "help":
				version()
				help()
				help_commands()
				continue
			if cmd == "list":
				list_help()
				continue
			if cmd == "get":
				get_help()
				continue
			if cmd == "get peers":
				print "getting peers..."
				continue
			if cmd == "list peers":
				print "listing peers..."
				continue
			if cmd == "commit":
				print "commiting changes..."
				continue
			if len(cmd) > 0:
				print "unknown command"

		print "Exiting main loop..."

if __name__ == "__main__":
    pass
