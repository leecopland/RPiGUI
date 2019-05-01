from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

## Hardware ##
led_red = LED(4)
led_green = LED(17)
led_blue = LED(22)

## GUI DEFINITIONS ##
win = Tk()
win.title('LED Toggler')

## Event Functions #
def ledToggle(led):
    turnOff()
    led.on()

def close():
    GPIO.cleanup()
    win.destroy()
    
def turnOff():
    led_red.off()
    led_green.off()
    led_blue.off()

## Widgets ##
var = IntVar()
redRadio = Radiobutton(win, text = 'Turn Red LED on', command = lambda: ledToggle(led_red), variable=var, value='Red').pack(anchor=tkinter.W)

blueRadio = Radiobutton(win, text = 'Turn Blue LED on', command = lambda: ledToggle(led_blue), variable=var, value='Blue').pack(anchor=tkinter.W)

greenRadio = Radiobutton(win, text = 'Turn Green LED on', command = lambda: ledToggle(led_green), variable=var, value='Green').pack(anchor=tkinter.W)

offRadio = Radiobutton(win, text = 'Turn all LED\'s off', command = turnOff, variable=var, value='Off').pack(anchor=tkinter.W)

exitButton = Button(win, text = 'Exit', command = close).pack(anchor=tkinter.W)

win.protocol("WM_DELETE_WINDOW", close) # exit cleanly

win.mainloop()