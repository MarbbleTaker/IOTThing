from machine import Pin, PWM
from utime import sleep
import random
import time

random_pitch = random.randrange(20,1000)
chosen_pitch = 0
has_answer_been_guessed = False
button = Pin(5, Pin.IN, Pin.PULL_UP)
button2 = Pin(22, Pin.IN, Pin.PULL_UP)
button3 = Pin(27, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(11))
random.randrange(20,1001)
score = 0
buzzer.freq(random_pitch)
buzzer.duty_u16(1000)
sleep (3)
buzzer.duty_u16(0)

while True:
    if button.value() == 0:
        chosen_pitch = chosen_pitch + 15 
        print (chosen_pitch)
        time.sleep(0.1)
        buzzer.freq(chosen_pitch)
        buzzer.duty_u16(1000)
        sleep (0.1)
        buzzer.duty_u16(0)
    else:
        sleep(0.2)
    if chosen_pitch > 1000:
        chosen_pitch = 20
    if button3.value() == 0:
        buzzer.freq(random_pitch)
        buzzer.duty_u16(1000)
        sleep (1)
        buzzer.duty_u16(0)
        buzzer.freq(chosen_pitch)
        buzzer.duty_u16(1000)
        sleep (1)
        buzzer.duty_u16(0)
    if button2.value() == 0:
        sleep (1)
        difference = abs(chosen_pitch - random_pitch)
        #print (difference)
        if difference < 15:
            buzzer.freq(1000)
            buzzer.duty_u16(1000)
            print ("you have no friends")
            sleep (1)
            buzzer.duty_u16(0)
            random_pitch = random.randrange(20,1000)
            buzzer.freq(random_pitch)
            buzzer.duty_u16(1000)
            sleep (3)
            buzzer.duty_u16(0)
            print (random_pitch)
            #light turns green
        else:
            print("you suck")
            buzzer.freq(1000)
            buzzer.duty_u16(1000)
            sleep (1)
            buzzer.duty_u16(0)
            random_pitch = random.randrange(20,1000)
            buzzer.freq(random_pitch)
            buzzer.duty_u16(1000)
            sleep (3)
            buzzer.duty_u16(0)
            print(difference)
        if button3.value() == 0:
            buzzer.freq(random_pitch)
            buzzer.duty_u16(1000)
            print ("you have no friends")
            sleep (3)
            buzzer.duty_u16(0)