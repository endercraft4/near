from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
import datetime
import os, fnmatch


#Needs Todo
	#

class Show_apps(object, QWidget):
	'''shows apps from list in Get.apps)'''
	
	def __init__(self, parent=None, iargs*):
		'''init args'''
		super(Show_apps, self)__init__*parent)
		
		
		for keyword in iargs:
			if keyword == "stay":
				self.playstay = keyword
			#elif 
			
	
	def apps(self, appstats*):
		'''shows app based on image and size, info(name, age, rating)'''
		for appstat in appstats:
			self.app_image = appstat("", or "/imgs/apps/default")
		
		
	def Get(object):
		'''Gets stuff for show apps (ie, apps, games, programming, ect)'''
		desktop_filesGamein = [] 
		for dirpath, dirs, apps, in os.walk("/usr/games/"):
			for name in fnmatch.filter(apps, '*.desktop'):
				desktop_filesGamein.append(name)


	def use(self, dirpath, app_N):
		'''uses applications files to decipher name, Icon, and uses <Terminal <2 soon>>.'''
		self.appAddress = dirpath + app_N
	
		self.app = []
		#with open(os.path.join(dirpath, app)):
		config.read(self.appAddress)
		
		try:
			#Append so as to have +2 var in each Var, (I.e, "Name of hsahdnians", " 2 2" Not "2", "2"
			self.app.append( config.get("Desktop Entry", "Name")) #extends the app var
			
			self.app.append(config.get("Desktop Entry", "GenericName"))
			 
			#[2] adds to specific location
			#self.app[2] = config.get
			self.app.append(config.get("Desktop Entry", "Type"))
			
			#categories
			self.app.append(config.get("Desktop Entry", "Categories"))
			
			#NoDisplay ? What is this? haha?
			selfapp.append(config.get("Desktop Entry", "NoDisplay"))
			
			#Icon for video game/ Application. is in SIZE = ?
			app.append(config.get("Desktop Entry", "Icon"))
		
		except: #not found one of these, write to Errors.ini Test for dev. Not too useful in normal.
			open_error_file = open ("Errors.ini", "a", 0)
			open_error_file.write(ValueError) #should not be ValueError.
			open_error_file.close()
		 


class Show(object, QWidget):
	'''shows apps from list in Get.apps)'''
	
	def __init__(self, parent=None, iargs*):
		'''init args'''
		#not s
		super(Show, self)__init__(parent)
		
		self.nameLine = QLineEdit()
		self.submitbutton = QPussButton("&amp;Submit")
		
		buttonLayout1 = QVBoxLayout()
		buttonLayout1.addWidget(nameLabel)#name
		
		
		self.submitbutton.clicked.connect(self.submitContact)
		
		mainLayout = QGridLayout()	
		# mainLayout.addWidget(nameLabel, 0, 0)
		mainLayout.addLayout(buttonLayout1, 0, 1)
		
		self.setLayout(mainLayout)
		self.setWindowTitle(none)#sets to none? expects "" probably?
		
	def submit_contact(self):
	
if __name__ == '__main__':
	import sys
	
	app = QApplication(sys.argv)
	
	screen = Show()
	screen.show()
	
	sys.exit((app.exec_())
	
