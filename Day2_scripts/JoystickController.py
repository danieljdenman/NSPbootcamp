#!/usr/bin/env python3
from pyfirmata import ArduinoMega, util
import glob

class JoystickController():
    def __init__(self,board_string,horizontal=0,vertical=1):
        self.board =  ArduinoMega(board_string)
        self.horizontal_channel = horizontal
        self.vertical_channel = vertical

        self.author_name = 'Daniel J Denman'

    def start(self):
        it = util.Iterator(self.board)
        it.start()
        self.board.analog[self.horizontal_channel].enable_reporting()#horizontal
        self.board.analog[self.vertical_channel].enable_reporting()#vertical
        #make an infinite loop
        print('ready to listen to joystick')
        while True:
            h = self.board.analog[0].read()
            v = self.board.analog[1].read()
            if h == None or v==None :pass
            else:
                if h < 0.4: #went left
                    self.left()
                if h > 0.6: #went right
                    self.right()
                if v < 0.4: #went up
                    self.up()
                if v > 0.6: #went down
                    self.down()

    def left(self):
        print('left')
    def right(self):
        print('right')
    def up(self):
        print('up')
    def down(self):
        print('down')

if __name__ == "__main__":
    board_port = glob.glob('/dev/cu.usbmodem*')[0]
    joystick=JoystickController(board_port)
    joystick.start()
