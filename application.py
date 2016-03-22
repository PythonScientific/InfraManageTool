""" Application Class
Base application class for timetable engine.

Author: 	Patryk Zabkiewicz
Date:		2016.03.21

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

class Application:
	def __init__(self):
		self.__private_value = 0
		self.start_time = 0
		self.running_time = 0
		self.configuration = list() # Configuration options container
		self.scheduler = Scheduler() # Job scheduler
		self.workers = list() # List of workers

	def recv_cmd(self):
		cmd = ""
		return cmd

	def mainloop(self):
		q = 1
		cmd = ""
		while q:
			cmd = recv_cmd()

			if cmd == "quit":
				q = 0
			 	pass 
