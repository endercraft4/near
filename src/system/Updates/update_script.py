#import sys for sys.exit() and os / datetime for recent updates
#time for timeing??
import sys; import datetime; import time

class Update_script(object):
	'''Update_script class.
Has update_get_snappy(),'''
	
	def __init__(self):
		'''Inits update args, if any.'''
		self.date_time = datetime.datetime()
		self.timer = none
		self.updates_available = []
		self.next_updates = 0 #not sure if a num/array
	
		
	def update_get(self):
		self.updates_available.append(self.update_get_snappy(self))
		#self.updates_available.append(update_get_debi())
		self.updates_available.append(self.update_get_sys(self)
		
	def update_get_snappy(self):
		os.system("sudo snappy update")#root?
		


	def update_get_sys(self): #?
		'''updates system snappy and debis'''
		os.system("")# not sure yet for snaps
		
		os.system("apt -y update")


	def update_main(self):
		self.update_get(self)


update_script = Update_script()
