import datetime
import ConfigParser



class Savedata(object):
	'''Savedata class.
has '''
	
	savedata_dir = "home/usr/savedata/" 
	savedata = []
	
	#savedata_see
	def savedate_see(self, save, args*):
		'''sees the save stuff within the file'''
		self.savefile_save = save
		self.getsection = args.getsection#how do I make this work []??
		self.us = args[us_option]# same as?
		self.us_option[self.us]
		
		sef.app = []
		
		config.read(self.savefile_save)
		
		if config.has_option(us):
			self.app.append(config.get(getsection, us_option))
		
		
		#return what player wan
		return  
