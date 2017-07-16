import RPi.GPIO as GPIO
from time import sleep
""" 
GPIO.setmode(GPIO.BCM)
 
Motor1A = 17
Motor1B = 23
Motor2A = 27
Motor2B = 22
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
"""
def pwm(y, one, two, t, smooth = True):
    GPIO.setmode(GPIO.BCM)
 
    Motor1A = 17
    Motor1B = 23
    Motor2A = 27
    Motor2B = 22
 
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    if one:
        m1a = Motor1A
        m1b = Motor1B
    else:
        m1b = Motor1A
        m1a = Motor1B
    if two:
        m2a = Motor2A
        m2b = Motor2B
    else:
        m2b = Motor2A
        m2a = Motor2B
    i = 0
    if smooth:
        y /= 100
        x = 0.1
    else:
        y /= 100
        x = y
    while i < t:
        GPIO.output(m1a,GPIO.HIGH)
        GPIO.output(m1b,GPIO.LOW)
        GPIO.output(m2a,GPIO.LOW)
        GPIO.output(m2b,GPIO.HIGH)
        sleep(x * 0.01)
        GPIO.output(m1a,GPIO.LOW)
        GPIO.output(m1b,GPIO.LOW)
        GPIO.output(m2a,GPIO.LOW)
        GPIO.output(m2b,GPIO.LOW)
        sleep(0.01*(1 - x))
        i += 1
        if smooth:
            if x < y:
                x += 0.005
    GPIO.cleanup()

def single_pwm(pwm,motor_bool,dir,time):
    GPIO.setmode(GPIO.BCM)
 
    Motor1A = 17
    Motor1B = 23
    Motor2A = 27
    Motor2B = 22
 
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    if motor_bool:
        if dir:
            ma = Motor1A
            mb = Motor1B
        else:
            ma = Motor1B
            mb = Motor1A
    else:
        if dir:
            mb = Motor2A
            ma = Motor2B
        else:
            mb = Motor2B
            ma = Motor2A
    pwm /= 100
    i=0
    while i < time:
        GPIO.output(ma,GPIO.HIGH)
        GPIO.output(mb,GPIO.LOW)
        sleep(pwm*0.01)
        GPIO.output(ma,GPIO.LOW)
        GPIO.output(mb,GPIO.LOW)
        sleep(0.01*(1 - pwm))
        i+=1
    GPIO.cleanup()


    



def go_right_laterally(offset):
   # offset=(int) offset
    offset *= 100
    num = (int)(offset/86)
    i=0
    while i < num:
        single_pwm(35,True,False,38)
        sleep(0.2)
        single_pwm(35,False,False,47)
        sleep(0.2)
        pwm(30,True,True,64,False)
        i+=1
        sleep(0.25)

def go_left_laterally(offset):
    #offset = (int) offset
    offset *= 100
    num = (int)(offset/78)
    i=0
    while i < num:
        single_pwm(35,False,False,36)
        sleep(0.2)
        single_pwm(35,True,False,37)
        sleep(0.2)
        pwm(30,True,True,85,True)
        i+=1
        sleep(0.25)
def forward(dist):
    time=dist/22.0
    pwm(50,True,True,time*100,False)

#pwm(40,True,True,100,False)

def turn_right(angle):
    rem = angle%10
    if(rem<=5 ):
        num = (int)(angle/10)
        
    else:

        num = (angle/10)+1

        if (angle<10.0 and angle > 6.0):
            num = 1
    i=0
    while i < num:
        pwm(25,True,False,25,False)
        i+=1
        sleep(1)

def turn_left(angle):
    rem = angle % 10
    if(rem<=5 ):
        num = (int)(angle/10)
    else:
        num = (angle/10)+1

        if (angle<10.0 and angle > 6.0):
            num = 1
    i=0
    while i < num:
        pwm(25,False,True,22,False)
        i+=1
        sleep(1)

def turnright_90():
        num=9
        i=0
        while i < num:
             pwm(50,True,False,4.1,False)
             i+=1

  
def turnleft_90():
    num = 9
    i=0

    while i < num:
         pwm(50,False,True,4.9,False)
         i+=1
def turn_180():
    turnright_90()
    sleep(1)
    turnright_90()

#forward(8.7)
#turn_180()
#forward(8.7)
#turn_left(90)

#go_left_laterally(2.00)
#go_right_laterally(2.00)
#forward(30)
#turn_left(90)
#forward(30)
pwm(100,False,True,1500,False)
#turnright_90()
"""
pwm(40, True, Te)
ue, 275)
pwm(50, False, True, 130, False)
pwm(40, True, True, 200)
pwm(50, False, True, 130, False)
"""
"""
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
sleep(2)"""
#GPIO.cleanup()