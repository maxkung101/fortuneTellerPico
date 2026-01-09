from machine import I2C, Pin
from time import sleep, sleep_ms
from machine_i2c_lcd import I2cLcd
import random

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
addr = i2c.scan()[0]
lcd = I2cLcd(i2c, addr, 2, 16)
pir_sensor = Pin(15, Pin.IN)

# Write your descriptions here.

# First line of the description
fortune1 = [
    "You get good    ",
    "You have a heart",
    "Success is on   ",
    "Your palm is an ",
    "Playing well is ",
    "Watch for birds "
]

# Second line of the description
fortune2 = [
    "luck.",
    "of gold.",
    "your way.",
    "A-OK.",
    "winning.",
    "coming soon."
]

def reset():
    lcd.putstr("I am a          ")
    lcd.putstr("Fortune Teller.")
    sleep(1)

def tellFortune():
    lcd.clear()
    x = random.randint(0, len(fortune1)-1)
    lcd.putstr(fortune1[x])
    lcd.putstr(fortune2[x])
    sleep(6)
    lcd.clear()

reset()

while True:
    reading = pir_sensor.value()
 
    if reading == 1:
        tellFortune()
        reset()
    else:
        pass