import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# define servo pins
x_servo_pin = 27  # X servo pin set to 27
y_servo_pin = 17 # Y servo pin set to 17

servo_frequency = 50

x_servo_pulse_range = (2.5, 12.5)
y_servo_pulse_range = (2.5, 12.5)

# Set PinMode
GPIO.setup(x_servo_pin, GPIO.OUT)
GPIO.setup(y_servo_pin, GPIO.OUT)

# Servo PWM instance
x_servo_pwm = GPIO.PWM(x_servo_pin, servo_frequency)
y_servo_pwm = GPIO.PWM(y_servo_pin, servo_frequency)

# X axis movement
def move_x(direction):
    if direction == "right":
        x_servo_pwm.start(x_servo_pulse_range[1])
    elif direction == "left":
        x_servo_pwm.start(x_servo_pulse_range[0])
    time.sleep(0.5)
    x_servo_pwm.stop()

# Y axis movement
def move_y(direction):
    if direction == "up":
        y_servo_pwm.start(y_servo_pulse_range[1])
    elif direction == "down":
        y_servo_pwm.start(y_servo_pulse_range[0])
    time.sleep(0.5)
    y_servo_pwm.stop()

try:
    while True:
        direction = input("Enter direction (x+/x-/y+/y-): ").lower()
        if direction == "x+":
            move_x("right")
        elif direction == "x-":
            move_x("left")
        elif direction == "y+":
            move_y("up")
        elif direction == "y-":
            move_y("down")
        else:
            print("Invalid direction. Try again!")

except KeyboardInterrupt:
    # Stop the program
    x_servo_pwm.stop()
    y_servo_pwm.stop()
    GPIO.cleanup()
