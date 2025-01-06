from tkinter import * #pip install tkinter
from PIL import Image,ImageTk,ImageSequence #pip install Pillow
import time
import pygame  #pip install pygame for sound 
from pygame import mixer
mixer.init()

root = Tk() #creates the main application window
root.geometry("1000x500") #set window dimension
def play_sound( s):
    #print('abc')
    mixer.music.load(s) #loads the audio file
    mixer.music.play()  #plays the audio file

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img #img is a global variable
    img = Image.open('comp-1.gif')
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    sound1='C:\\himanshi\\EVE_FINAL\\cute-character-wee-3-188163.mp3'
    play_sound(sound1)
    #sound1.play()
    #time.sleep(sound1.get_length())
    sound2='C:\\himanshi\\EVE_FINAL\\voice.mp3'
    play_sound(sound2)
    #sound2.play()
    #time.sleep(sound2.get_length())
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.005)
    root.destroy()

play_gif()
root.mainloop() #ensures the GUI remains active until the animation ends or the user closes the window.
