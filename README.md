# RaspberryArduinoServo

## CURRENTLY IN DEVELOPMENT


<img src="https://raw.githubusercontent.com/mihaialexandruteodor/mihaialexandruteodor/master/repoImages/RaspberryArduinoServo/stage1.jpg"
     alt="stage 1"
     width=50% height=50% />

<img src="https://raw.githubusercontent.com/mihaialexandruteodor/mihaialexandruteodor/master/repoImages/RaspberryArduinoServo/stage2.jpg"
     alt="stage 2"
     width=50% height=50% />

Project that controls 4 DC motors using a Raspberry 4 and an Arduino Uno

## Purpose
As the code serves to provide an universal software control mechanism, the only limit is the user's imagination.
A good example of an use case is a 2-axis Gantry robot, with two of the DC motors providing x-axis movement, and the other two providing y-axis movement.
<img src="https://www.azorobotics.com/images/equipments/EquipmentImage_271.jpg"
     alt="gantry"
     width=50% height=50% />

## Specs
| **Component** | **Model** |
| ------------- | --------- |
| Raspberry PI 4 | 1gb RAM |
| Arduino | R3 ATmega328P |
| Quad DC Motor Shield | SKU DRI0039 |
| USB Cable | USB 2.0 A Male to B Male Scanner Cord|
| DC Motors x4 |  |

---------------------- 

How to start:
- [x] Install Raspberry OS on your Raspberry Pi 

<https://www.raspberrypi.org/documentation/installation/installing-images/README.md>
- [x] Connect your Arduino Uno to your Raspberry via USB cable (printer cable)
- [x] Log into Raspberry OS, headless through SSH or using a monitor
- [x] On Raspbian, create a folder for the repo
- [x] Clone using
```
git clone https://www.github.com/mihaialexandruteodor/RaspberryArduinoServo    
```
- [x] Run the main.py file (this will also install the sketch on your Arduino)
```
python main.py
```
- [x] Run the reset.py if you need to clear the Arduino memory
```
python reset.py
```


Thanks:
https://makerprojekt.com/portfolio/python-arduino-servo-control/
