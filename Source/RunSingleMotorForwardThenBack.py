#!/usr/bin/python

import PiMotor
import time
import RPi.GPIO as GPIO

motorCount = 4

motors = []
arrows = []

for motorIndex in range(motorCount):
    
    motorNumber = motorIndex + 1
    motorName = "MOTOR" + str(motorNumber)
    motor = PiMotor.Motor(motorName, 1)
    motors.append(motor)
    
    arrowNumber = motorNumber
    arrow = PiMotor.Arrow(arrowNumber)
    arrows.append(arrow)

try:
    motorToRunIndex = 3
    motorToRunNumber = motorToRunIndex + 1

    motorToRun = motors[motorToRunIndex]
    arrowForward = arrows[2]
    arrowReverse = arrows[0]
    secondsToRunMotor = 3
    speedToRunMotorAtAsPercentage = 50
    
    arrowForward.on()
    motor.forward(speedToRunMotorAtAsPercentage)
    time.sleep(secondsToRunMotor)
    motor.stop()
    arrowForward.off()

    arrowReverse.on()
    motor.reverse(speedToRunMotorAtAsPercentage)
    time.sleep(secondsToRunMotor)
    motor.stop()
    arrowReverse.off()
        
except KeyboardInterrupt:
    GPIO.cleanup()

    
