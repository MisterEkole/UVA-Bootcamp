from djitellopy import tello
from time import sleep

me = tello.Tello()
print(me.get_battery())

me.takeoff()
me.flip_left()
sleep(5)
me.flip_right()
sleep(5)
me.land()
