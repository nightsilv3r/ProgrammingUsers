#Übung1

#import von Packeten
import pyautogui

#PyAutoguy Optionen
pyautogui.PAUSE = 0.05

#Variable
distance = 200
duration = 0.05
steps = 10

pyautogui.mouseDown()
pyautogui.mouseUp()

while distance >= 0:
	##############################################################
	
	pyautogui.drag(distance, 0, duration=duration, button='left')
	pyautogui.drag(0, distance, duration=duration, button='left')
	pyautogui.drag(-distance, 0, duration=duration, button='left')
	pyautogui.drag(0, -distance, duration=duration, button='left')
	
	distance = distance - steps

	##############################################################


