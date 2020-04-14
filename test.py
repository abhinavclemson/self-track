import psutil
import subprocess
import AppKit
from AppKit import NSWorkspace
from collections import defaultdict

#pl = subprocess.run(['ls', '-la']))
dict=defaultdict(float)
res=[]


try:
	while True:
		#for p in psutil.process_iter():
		#	dict[p.name()]+=0.001
		#print(dict)
#		active_app_name = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()
		activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
		dict[activeAppName]+=1
		
		print(dict)
except keyboardInterrupt:
		pass
		
		 


