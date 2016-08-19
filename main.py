### Author: Peter Fox and Ryan Field
### Description: Head Sup!
### Category: Games
### License: MIT
### Appname: Head Sup!
### Built-in: yes

import pyb
import math
import ugfx
import buttons
import machine

ugfx.init()
buttons.init()
buttons.disable_menu_reset()

def splash():
    changePixel(0x00BFFF)
    ugfx.area(0,0,ugfx.width(),ugfx.height(),ugfx.html_color(0xC390D4))
    ugfx.set_default_font(ugfx.FONT_TITLE)
    ugfx.display_image(0,10, "apps/headsup/headsupsplash.gif")
    ugfx.text(30, 190, "Head Sup ", ugfx.RED)
    ugfx.text(30, 215, "Press A to Continue ", ugfx.GREEN)
    while True:
        pyb.wfi()
        if buttons.is_triggered("BTN_A"):
            break
        if buttons.is_triggered("BTN_MENU"):
            playing = 0 #pyb.hard_reset()
            break
        

def menu():
    ugfx.area(0,0,ugfx.width(),ugfx.height(),ugfx.html_color(0x90C3D4))
    ugfx.set_default_font(ugfx.FONT_TITLE)
    ugfx.text(30, 30, "Select a subject:", 0xFFFF)
    while True:
        pyb.wfi()
        if buttons.is_triggered("BTN_A"):
            return 0
        if buttons.is_triggered("BTN_MENU"):
            playing = 0 #pyb.hard_reset()
            break

def loadGame(level):
    if level == 0:
        ugfx.area(0,0,ugfx.width(),ugfx.height(),ugfx.html_color(0x90C3D4))
        ugfx.set_default_font(ugfx.FONT_TITLE)
        ugfx.text(30, 30, "Food: ", 0xFFFF)
        changePixel(0xFF0000)
        pyb.delay(1000)
        ugfx.area(0,0,ugfx.width(),ugfx.height(),ugfx.html_color(0x90C3D4))
        ugfx.text(30, 30, "Starting in: ", 0xFFFF)
        changePixel(0xFF6600)
        #timer1 = pyb.Timer(2)
        #timer1.init(freq=1)
        totalTime = 5
        timer1 = pyb.Timer(2, prescaler=83, period=0x3fffffff)
        timer1.counter(0)
        s=ugfx.Style()
        s.set_background(ugfx.html_color(0x90C3D4))
        loadingContainer = ugfx.Container(0,30, 320, 30)
        loadingContainer.show()
        loadingContainer.area(0,0,320,30,ugfx.html_color(0x90C3D4))
        loadingContainer.text(0, 0, "Starting in: ", 0xFFFF)
        ugfx.set_default_font(ugfx.FONT_NAME)
        loadingContainerCount = ugfx.Container(0,60, 320, 180)
        loadingContainerCount.show()
        loadingContainerCount.area(0,0,320,180,ugfx.html_color(0x90C3D4))
        
        while True:
            currentTime = timer1.counter()
            count = currentTime / 1000000
            if count < 5:
                loadingContainerCount.area(0,0,320,180,ugfx.html_color(0x90C3D4))            
                dispTime = totalTime - count
                #ugfx.area(0,0,ugfx.width(),ugfx.height(),ugfx.html_color(0x90C3D4))
                #ugfx.Label(20,0,300,160," %d " % (dispTime),parent=loadingContainerCount, justification=ugfx.Label.CENTER, style=s)
                dispTimeInt = int(dispTime)
                if dispTimeInt%2==0:
                    changePixel(0xFF0000)
                    ugfx.text(130,100," %d " % (dispTime),ugfx.RED)
                else:
                    changePixel(0xFF6600)
                    ugfx.text(130,100," %d " % (dispTime),ugfx.ORANGE)
                pyb.delay(60)
            else:
                break
        while True:
            pyb.wfi()
            if buttons.is_triggered("BTN_A"):
                return 0
            if buttons.is_triggered("BTN_MENU"):
                playing = 0 #pyb.hard_reset()
                break
            
def changePixel(color):
    pin = machine.Pin("PB13", machine.Pin.OUT)
    neo = pyb.Neopix(pin)
    neo.display(color)

playing = 1
while playing:
    splash()
    level = menu()
    score = loadGame(level)
    ugfx.area(0,0,ugfx.width(),ugfx.height(),0)
    ugfx.text(30, 30, "Round Over Score: %d " % (score), 0xFFFF)
    ugfx.text(30, 60, "Press A to play again ", 0xFFFF)
    ugfx.text(30, 90, "Press MENU to quit " , 0xFFFF)
    while True:
        pyb.wfi()
        if buttons.is_triggered("BTN_A"):
            break

        if buttons.is_triggered("BTN_MENU"):
            playing = 0 #pyb.hard_reset()
            break