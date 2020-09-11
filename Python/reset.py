""" Mihai Alexandru Teodor 2020 """

import serial   
import os
from pathlib import Path

ser = serial.Serial('/dev/ttyACM0', 115200)
ser.isOpen()

dir_path = os.path.dirname(os.path.realpath(__file__))
path = Path(dir_path)
dir_path = str(path.parent) + "/Arduino/empty/empty.ino.standard.hex"

os.system("sudo avrdude -p m328p -c arduino -P //dev//ttyACM0 -b 115200 -U flash:w:"+dir_path+":i")