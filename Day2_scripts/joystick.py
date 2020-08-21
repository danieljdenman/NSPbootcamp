#connect to a piece of hardware, in this case an Arduino with a jooystick
from pyfirmata import ArduinoMega, util

#get the board
board = ArduinoMega('/dev/cu.usbmodem1412201')

#set up which pins on the board we want to check
it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()#horizontal
board.analog[1].enable_reporting()#vertical

#make an infinite loop
print('ready to listen to joystick')
while True:
    h = board.analog[0].read()
    v = board.analog[1].read()
    if h == None or v==None :pass
    else:
        if h < 0.4: #went left
            print('went left')

        if h > 0.6: #went right
            print('went right')

        if v < 0.4: #went up
            print('went up')

        if v > 0.6: #went down
            print('went down')
