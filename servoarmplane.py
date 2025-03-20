# Write your code here :-)
from machine import ADC, Pin, PWM
import time

# Setup the flex sensor pin
flex_sensor1 = ADC(Pin(27))  # GPIO 14
flex_sensor1.atten(ADC.ATTN_11DB)  # Full range: 0-3.3V

flex_sensor2 = ADC(Pin(14))
flex_sensor2.atten(ADC.ATTN_11DB)

flex_sensor3 = ADC(Pin(32))
flex_sensor3.atten(ADC.ATTN_11DB)

motor_1 = PWM(Pin(12))
motor_1.freq(50) #amount of times it will oscillate per second so basically 50 hertz.

motor_2 = PWM(Pin(4))
motor_2.freq(50)

motor_3 = PWM(Pin(2))
motor_3.freq(50)

def map_function(val1, inputMin, inputMax, outputMin, outputMax):
    result = int((val1 - inputMin) * (outputMax - outputMin) / (inputMax - inputMin) + outputMin)
    #result = y
    #val1 - inputMin = x
    #(outputMax - outputMin) / (inputMax - inputMin) = m
    #outputMin = c
    return max(outputMin, min( outputMax, int(result)))

while True:
    sensor_value1= flex_sensor1.read()  # Read the analog value
    #print("Flex Sensor Value:", sensor_value)
    #time.sleep(0.5)

    sensor_value2= flex_sensor2.read()
    sensor_value3= flex_sensor3.read()

    angle1 = map_function(sensor_value1, 2500, 3000, 26, 128)
    angle2 = map_function(sensor_value2, 2500, 3000, 26, 128)
    angle3 = map_function(sensor_value3, 2500, 3000, 26, 128)


    #print("sensor value1:", sensor_value1, " angle1:", angle, "sensor value2:", sensor_value2, " angle2:", angle2)
    motor_1.duty(angle1)
    motor_2.duty(angle2)
    motor_3.duty(angle3)

    time.sleep(0.5)

# Write your code here :-)
