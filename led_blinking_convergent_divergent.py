import RPi.GPIO as xyz
import time
xyz.setmode(xyz.BOARD)
xyz.setwarnings(False)
xyz.setup(3,OUT)
xyz.setup(5,OUT)
xyz.setup(7,OUT)
xyz.setup(11,OUT)
xyz.setup(12,OUT)
xyz.setup(13,OUT)
xyz.setup(15,OUT)
xyz.setup(18,OUT)
a=[3,5,7,11,12,13,15,18]
while 1:
    for i in range(0,8):
        xyz.output(a[i],1)
        xyz.output(a[i-1],1)
        time.sleep(1)
