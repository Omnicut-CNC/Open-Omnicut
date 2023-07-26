import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin used for servo control
servo_pin = 17

# Set the frequency for the PWM signal (50 Hz is typical for servos)
frequency = 50

# Setup the GPIO pin as an output
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM object with the servo pin and frequency
pwm = GPIO.PWM(servo_pin, frequency)

# Function to set the servo position
def set_servo_position(position):
    # Map the position value to the duty cycle (0 to 100)
    duty_cycle = 2 + (position / 18)
    pwm.ChangeDutyCycle(duty_cycle)

# Start the PWM signal with 0 position (servo at minimum)
pwm.start(0)

try:
    while True:
        # Move the servo to position 0 (0 degrees)
        set_servo_position(0)
        time.sleep(1)

        # Move the servo to position 90 (90 degrees)
        set_servo_position(90)
        time.sleep(1)

        # Move the servo to position 180 (180 degrees)
        set_servo_position(180)
        time.sleep(1)

except KeyboardInterrupt:
    pass

# Clean up the GPIO settings
pwm.stop()
GPIO.cleanup()