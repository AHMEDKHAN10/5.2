from tkinter import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.output(29, GPIO.LOW)
GPIO.output(31, GPIO.LOW)
GPIO.output(33, GPIO.LOW)
win = Tk()

def LED_1():
    print ("LED button pressed")
    if GPIO.input(29):
        GPIO.output(29, GPIO.LOW)
    else:
        GPIO.output(29, GPIO.HIGH)

def LED_2():
    print ("LED button pressed")
    if GPIO.input(31):
        GPIO.output(31, GPIO.LOW)
    else:
        GPIO.output(31, GPIO.HIGH)
        
def LED_3():
    print ("LED button pressed")
    if GPIO.input(33):
        GPIO.output(33, GPIO.LOW)
    else:
        GPIO.output(33, GPIO.HIGH)

def ExitProgram():
    print("Exit Button Pressed")
    GPIO.cleanup()
    win.quit()
    
win.title("First GUI")

ExitButton = Button(win, text = "EXIT",  command = ExitProgram, height = 2, width =  8)
ExitButton.pack(side = BOTTOM)

ledButton = Button(win, text = "LED 1",  command = LED_1, height = 2, width =  8)
ledButton.pack()
ledButton = Button(win, text = "LED 2",  command = LED_2, height = 2, width =  8)
ledButton.pack()
ledButton = Button(win, text = "LED 3",  command = LED_3, height = 2, width =  8)
ledButton.pack()

mainloop()
    