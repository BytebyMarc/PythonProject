from time import sleep

import keyboard

while True:

	match keyboard.read_key():

		case "nach-oben":
			print("Oben")

		case "nach-unten":
			print("Unten")

		case "nach-links":
			print("Links")

		case "nach-rechts":
			print("Rechts")

	sleep(0.1)


