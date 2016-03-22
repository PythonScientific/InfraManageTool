""" Route Engine
This project is intended to provide server management engine written in Python

Author: Patryk Zabkiewicz
Date:	2016.03.21

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

from application import *
import argparse

if __name__ == "__main__":
		parser = argparse.ArgumentParser(description='Process some integers.')
		parser.add_argument('integers', metavar='N', type=int, nargs='+',
		                   help='an integer for the accumulator')
		parser.add_argument('--sum', dest='accumulate', action='store_const',
		                   const=sum, default=max,
		                   help='sum the integers (default: find the max)')

		args = parser.parse_args()
		print args.accumulate(args.integers)

		app = Application()
		app.mainloop()

