""" Timetable
This project is intended to provide server management engine written in Python

Author: Patryk Zabkiewicz
Date:	2016.03.21

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

import os
import argparse
from application import *

current_dir = os.path.dirname(os.path.realpath(__file__))
config_file_path = ""

VERSION = "ver.0.01"

def help():
	print "The program stores current server status and by exchanging information"
	print " with it's peers it execute changes to this machine"

def version():
	print "Timetable "+VERSION+" Alpha"

if __name__ == "__main__":
		parser = argparse.ArgumentParser(description=version())
		#parser.add_argument('integers', metavar='N', type=int, nargs='+',
		#                   help='an integer for the accumulator')
		parser.add_argument('--config_file', action='store_const',
		                   const=config_file_path, default=os.path.join(current_dir,".timetable","default.config"),
		                   help='config file path (default: .imt/default.config)')

		args = parser.parse_args()

		print "Engine is starting..."

		app = Application()
		app.init()
		app.mainloop()

		print "Engine has stopped"
