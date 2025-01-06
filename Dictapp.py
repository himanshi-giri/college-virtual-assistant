import os 
import pyautogui #control the mouse, keyboard, and perform GUI automation tasks
import webbrowser #allows to launch a web browser and open urls directl
import pyttsx3 
from time import sleep


engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt","camera": "WindowsCamera"  }

def openappweb(query):
    speak("opening, sir")
    if ".com" in query or "co.in" in query:
        query = query.replace("open","")
        query = query.replace("eve","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys :
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("closing sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
    elif "2 tab " in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak ("all tabs closed")

    elif "3 tab " in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak ("all tabs closed")
        pyautogui.hotkey("ctrl","w")
        speak ("all tabs closed")

    elif "4 tab " in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak ("all tabs closed")
        pyautogui.hotkey("ctrl","w")
        speak ("all tabs closed")
        pyautogui.hotkey("ctrl","w")
        speak ("all tabs closed")

    elif "5 tab " in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak ("all tabs closed")
        pyautogui.hotkey("ctrl","w")
        speak ("all tabs closed")
        pyautogui.hotkey("ctrl","w")
        speak ("all tabs closed")
        pyautogui.hotkey("ctrl","w")
        speak ("all tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
    


    