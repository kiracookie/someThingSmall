import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
Motor1A = 11
Motor1B = 12
Motor1E = 16 	#使能通道A

Motor2A = 13
Motor2B = 15
Motor2E = 18 	#使能通道B


#print("Setting up GPIO pins")
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)


#print("Warming up engines")
motorR = GPIO.PWM(Motor1E,100)
motorL = GPIO.PWM(Motor2E,100)
#print("Starting motors")

def initStart():
    motorR.start(0)
    motorL.start(0)

def checkSpeed(speed):
    print("Checking the speed")
    if speed < 25:
        speed = 25
    if speed > 100:
        speed = 100
    print("Speed is: "+str(speed))
    return speed

def goStraight(speed):
    speed = checkSpeed(speed)
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    motorR.ChangeDutyCycle(speed)
    motorL.ChangeDutyCycle(speed)
    print("Going straigh with speed: "+str(speed))
#time.sleep(100)

def stop():
    print("Stoping")
    GPIO.output(Motor1A, False)
    GPIO.output(Motor1B, False)
    GPIO.output(Motor2A, False)
    GPIO.output(Motor2B, False)
    motorR.ChangeDutyCycle(0)
    motorL.ChangeDutyCycle(0)

def exitAndClean():
    print("Exiting")
    motorR.stop()
    motorL.stop()
    GPIO.cleanup()
    exit()

def cleanNoExit():
    print("Exiting")
    motorR.stop()
    motorL.stop()
    GPIO.cleanup()

def goBack(speed):
    speed = checkSpeed(speed)
    print("Going back with speed: "+str(speed))
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    motorR.ChangeDutyCycle(speed)
    motorL.ChangeDutyCycle(speed)

def turnRight(speed):
    speed = checkSpeed(speed)
    print("Turning right with speed: "+str(speed))
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, False)
    GPIO.output(Motor2B, False)
    motorR.ChangeDutyCycle(80)
    motorL.ChangeDutyCycle(80)

def turnLeft(speed):
    speed = checkSpeed(speed)
    print("Turning left with speed: "+str(speed))
    GPIO.output(Motor1A, False)
    GPIO.output(Motor1B, False)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    motorR.ChangeDutyCycle(80)
    motorL.ChangeDutyCycle(80)