import cv2
import os
import time

PREFIX_MESSAGE = ""
SUFFIX_MESSAGE = ""
PINK_MODE = False

COLORS = {
	"BRIGHT_WHITE": "\033[97m",
	"BRIGHT_CYAN": "\033[96m",
	"WHITE": "\033[37m",
	"CYAN": "\033[36m",
	"RESET": "\033[39m"
}


if PINK_MODE:
	COLORS["BRIGHT_CYAN"] = "\033[95m"
	COLORS["CYAN"] = "\033[35m"
	COLORS["RESET"] = "\033[33m"

gif = cv2.VideoCapture("./dolphin.gif")
success,img = gif.read()

frames = []

TCOLUMNS, TROWS = os.get_terminal_size(0)
while success:
	rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
	gray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
	frames.append(cv2.resize(gray,(TROWS,TROWS)))
	success,img = gif.read()

def display_frames():
	i = 0
	while True:
		os.system("clear")
		if i >= len(frames)-1:
			i = 0

		for y in range(TROWS):
			to_display = "%s%s"%(COLORS["RESET"],PREFIX_MESSAGE)
			for x in range(TROWS):
				PIXEL = frames[i][x,y]
				if PIXEL < 20:
					to_display += "%s "%COLORS["BRIGHT_WHITE"]
				elif PIXEL < 127:
					to_display += "%s!"%COLORS["BRIGHT_CYAN"]
				elif PIXEL < 200:
					to_display += "%s@"%COLORS["CYAN"]
				else:
					to_display += "%s."%COLORS["WHITE"]

			to_display+="%s%s"%(COLORS["RESET"],SUFFIX_MESSAGE)

			print(to_display)
		i+=1
		time.sleep(0.12)

display_frames()