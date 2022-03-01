#basic controls or tello drone using python


from djitellopy import tello #importing the djitellopy library
 
from time import sleep
 
me = tello.Tello() #instantiating our tello class to variable me
 
me.connect() #here enabling connection with drone #make sure your PC is connected to drone via WiFi
 
print(me.get_battery())
 
me.takeoff()
 
me.send_rc_control(0, 50, 0, 0)
 
sleep(2)
 
me.send_rc_control(0, 0, 0, 30)
 
sleep(2)
 
me.send_rc_control(0, 0, 0, 0)
 
me.land()