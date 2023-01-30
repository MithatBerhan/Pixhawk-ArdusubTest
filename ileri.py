import sys
from pymavlink import mavutil

master = mavutil.mavlink_connection( # Pixhawk bağlantısı
            '/dev/ttyACM0',
            baud=115200)

def set_rc_channel_pwm(id, pwm=1500): #çift yönlü motor için 0 durumunda PWM=1500

    if id < 1:
        print("Channel does not exist.")
        return


    if id < 9: # ardusubla iletisim
        rc_channel_values = [65535 for _ in range(8)]
        rc_channel_values[id - 1] = pwm
        master.mav.rc_channels_override_send(
            master.target_system,
            master.target_component,
            *rc_channel_values)
	
#Pixhawk'ın motorları çalıştırabilmesi için Arm edilir.
	    
master.mav.command_long_send( 
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0) 

#Motor düzeni Vectored ROV
    
def ileri():
    set_rc_channel_pwm(1, 1650)
    set_rc_channel_pwm(2, 1650)    
def geri():
    set_rc_channel_pwm(2, 1400)
    set_rc_channel_pwm(4, 1450)
def sol():
    set_rc_channel_pwm(2, 1600)
    set_rc_channel_pwm(4, 1400)
def sag():
    set_rc_channel_pwm(1, 1600)
    set_rc_channel_pwm(3, 1400)
def alcal():
    set_rc_channel_pwm(5, 1550)
    set_rc_channel_pwm(6, 1350)
def yuksel():
    set_rc_channel_pwm(5, 1350)
    set_rc_channel_pwm(6, 1550)
def don():
    set_rc_channel_pwm(1, 1400)
    set_rc_channel_pwm(2, 1400)
    set_rc_channel_pwm(3, 1600)
    set_rc_channel_pwm(4, 1600)

git = 0
while(True):
	if(4500 > git):
		yuksel()
		ileri()
		git +=1
		print(git)
	elif(4501 < git < 6000 ):
		sol()
		git +=1
		print(git)

else:
    	alcal()
