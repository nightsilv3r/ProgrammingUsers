#import von Packeten
import pyautogui, time
from PIL import Image
import requests
from io import BytesIO
import numpy
from scipy.interpolate import interp1d

#PyAutoguy Optionen
pyautogui.PAUSE = 0.02

#Bildquelle
#INPUTS//////////////////////////////////////////
url= input('img-url: ')
#Schrittlänge
distance = int(input('PixelSize: '))
ogDistance = distance
#Verzerrt das Bild auf X
imgSizeX = int(input('PixelsX: '))
#Verzerrt das Bild auf Y
imgSizeY = int(input('PixelsY: '))
#Modus Auswahl
mode = int(input('mode: '))
#Bild Laden
bild = requests.get(url)
im = Image.open(BytesIO(bild.content))

#Auflösung
#INPUTS//////////////////////////////////////////
#Fokus ins Fenster legen
pyautogui.mouseDown()
pyautogui.mouseUp()

#Pixel unseres Bildes werden angepasst und als Array ausgegeben
im2 = im.resize((imgSizeX, imgSizeY), Image.NEAREST) 
imageArray = numpy.array(im2)
# Variablen zum durchlaufen der Pixel
actualPixel = -1
pixelcounter = 0
#Loop durch das Bild
for row in imageArray:
	#Für jeden Pixel in jeder Reihe...
	for pix in row:
		actualPixel = actualPixel +1
		average = numpy.mean(pix)

		#steps = 255/average
		#Gibt durchschnittsfarbwert aus
		print(average)

		#Map Function Für die Farbwerte 0-255 auf die Werte 0-10
		start1 = 0
		stop1 = 255
		start2 = 0
		stop2 = distance

		#Zeit Pro Pinselstrich: Hier muss man durch herantasten die Grenzen des Zeichenprogrammes austesten, Photoshop braucht z.B. viel länger als Paint
		duration = 0.05

		steps = ((average-start1)/(stop1-start1))*(stop2-start2)+start2

		#Verhindere teilen durch 0
		if steps < 1:
			steps = 1

		#Eigentliches Zeichnen im jeweiligen Pixel

		while distance >= 0:
		#Modeus 1
			if mode == 1:

				pyautogui.drag(distance, 0, duration=duration, button='left')
				pyautogui.drag(0, distance, duration=duration, button='left')
				pyautogui.drag(-distance, 0, duration=duration, button='left')
				pyautogui.drag(0, -distance, duration=duration, button='left')
				distance = distance - steps
		
		#Modus2
			if mode == 2:

				pyautogui.drag(distance, 0, duration=duration, button='left')
				pyautogui.drag(0, distance, duration=duration, button='left')
				pyautogui.drag(-distance, -distance, duration=duration, button='left')
				distance = distance - steps

		#Modus3
			if mode == 3:
				#####################################################
				#Variabeln die man verwenden kann:
				#distance (Schrittlänge)
				#steps (Schrittlänge/Grauwert = Steps)
				#pyautogui.drag(zielX, zielY, duration=duration, button='left')
				#####################################################
				print('mein Modus')
				distance = distance - steps
				#####################################################

		distance = ogDistance

		if (actualPixel+1) % imgSizeX == 0:
			pyautogui.move(-distance*imgSizeX+distance, distance)
		else:
			pyautogui.move(distance, 0)	



