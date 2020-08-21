import os,sys, glob
sys.path.append(os.path.join(os.getcwd(),'JoystickController.py'))
from JoystickController import JoystickController

from playsound import playsound


class JoystickControllerSound(JoystickController):

    def left(self):
        playsound('/System/Library/Sounds/Funk.aiff')
    def right(self):
        playsound('/System/Library/Sounds/Basso.aiff')
    def up(self):
        playsound('/System/Library/Sounds/Ping.aiff')
    def down(self):
        playsound('/System/Library/Sounds/Sosumi.aiff')

if __name__ == "__main__":
    d=JoystickControllerSound(glob.glob('/dev/cu.usbmodem*')[0])
    d.start()
