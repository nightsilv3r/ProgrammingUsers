import pyautogui, time

time.sleep(0)
pyautogui.click()    # click to put drawing program in focus

kante = 400
schritte = 15

pyautogui.mouseDown()
pyautogui.mouseUp()

while kante > 0:
	pyautogui.dragRel(kante, 0, duration=0, button='left')   # move right
	kante = kante - schritte
	pyautogui.dragRel(0, kante, duration=0, button='left')   # move down
	pyautogui.dragRel(-kante, 0, duration=0, button='left')  # move left
	kante = kante - schritte
	pyautogui.dragRel(0, -kante, duration=0, button='left')  # move upwhile countX < scale:

	while countY < scale:

		while distance > 0:
			pyautogui.drag(distance, 0, duration=0, button='left')   # move right
			pyautogui.drag(0, distance, duration=0, button='left')   # move right
			pyautogui.drag(-distance, 0, duration=0, button='left')   # move right
			pyautogui.drag(0, -distance, duration=0, button='left')   # move right

			distance = distance - steps

		countY = countY +1
		distance = ogDistance
		pyautogui.move(distance, 0)

	countX = countX +1
	countY = 0
	distance = ogDistance
	pyautogui.move(-distance*scale, distance)