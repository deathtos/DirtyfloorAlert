import sys
from datetime import datetime
from time import sleep
from DirtyFloor_Motion import beginMonitor

sleepTime = 3

widthH = 2592 # too slow for motion check, only use for the save sequence 
heightH = 1944

try:
    while True:
        saveImages(widthH,heightH)
		
except:
    print("Error: ", sys.exc_info()[0])
    print()	




