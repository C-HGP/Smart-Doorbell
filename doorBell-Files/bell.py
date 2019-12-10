
import time
import sys, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

button = 17
counter = 0
end = 1200000
stop = False
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time.sleep(0.5)

while True:
	input_state = GPIO.input(button)

	if input_state == False:
		#os.system("raspistill -o /var/www/html/image.jpg -t 100")
		#os.system("cd camera/mjpg-streamer/mjpg-streamer-experimental/")
		stop = True
		os.system("cd camera/mjpg-streamer/mjpg-streamer-experimental/ && ./mjpg_streamer -o \"output_http.so -w ./www\" -i \"input_raspicam.so\" &")
		os.system("mosquitto_pub -h 192.168.10.71 -t bell -m \"on\"")
		os.system("echo running")
		time.sleep(0.3)
		

	if stop == True:
		counter += 1
		
		if counter == end:
			os.system("sudo killall mjpg_streamer")
			counter = 0
			stop = False
