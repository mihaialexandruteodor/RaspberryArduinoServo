""" Mihai Alexandru Teodor 2020 """

from serial import Serial
from subprocess import run
import struct
import time
import os
from os import system, name 
from pathlib import Path

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


dir_path = os.path.dirname(os.path.realpath(__file__))
path = Path(dir_path)
dir_path = "flash:w:"+ str(path.parent) + "/Arduino/sketch/sketch.ino.standard.hex:i"

Serial('/dev/ttyACM0', 115200).close()
time.sleep(1)

run(["avrdude", "-p", "m328p", "-c", "arduino", "-P", "//dev//ttyACM0", "-b", "115200", "-U", dir_path])
time.sleep(2)

ser = Serial('/dev/ttyACM0',9600)
ser.reset_output_buffer()
ser.flush()
ser.close()

time.sleep(2)
ser.open()

while True:
	clear()
	print("1 - forward x axis\n")
	print("2 - backward x axis\n")
	print("3 - forward y axis\n")
	print("4 - backward y axis\n")
	command = str(input ("instruction: "))
	ser.write(command.encode())
