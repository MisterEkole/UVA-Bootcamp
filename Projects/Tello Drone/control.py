from djitellopy import tello
import Keypressmodule as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 100;
    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed
    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed
    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed
    if kp.getKey("a"):
        yv = -speed
    elif kp.getKey("d"):
        yv = speed
    if kp.getKey("q"):
        me.land()
        sleep(3)
    if kp.getKey("e"):
        me.takeoff()
    if kp.getKey("k"):
        me.flip_back()
    if kp.getKey("i"):
        me.flip_forward()
    if kp.getKey("j"):
        me.flip_left()()
    if kp.getKey("l"):
        me.flip_right()
    if kp.getKey("f"):
        me.flip_left()
        sleep(1)
        me.flip_right()
        sleep(1)
        me.flip_forward()
        sleep(1)
        me.flip_back()
    if kp.getKey("g"):
        me.flip_back()
        sleep(.5)
        me.flip_back()
        sleep(.5)
        me.flip_back()
    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)