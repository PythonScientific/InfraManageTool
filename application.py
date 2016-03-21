#!/usr/bin/env python
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

	def mainloop():
		q = 1
		cmd = ""
		while q:
			cmd = recv_cmd()

			if cmd == "quit":
				q = 0
			 	pass 
