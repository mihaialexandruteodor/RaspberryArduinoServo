""" Mihai Alexandru Teodor 2020 """

import serial   
import os
import struct
import time
from pathlib import Path


dir_path = os.path.dirname(os.path.realpath(__file__))
path = Path(dir_path)
dir_path = str(path.parent) + "/Arduino/sketch/sketch.ino.standard.hex"

os.system("sudo avrdude -p m328p -c arduino -P //dev//ttyACM0 -b 115200 -U flash:w:"+dir_path+":i")

time.sleep(1)

Serial('/dev/ttyACM0',baudrate=115200).close()

time.sleep(1)

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:                                            
        #command = str(input ("instruction: "))      
        command = 1
        ser.write(struct.pack('B', command))                          
        reachedPos = str(ser.readline())            
        print(reachedPos)       