#calculatenumbers.py

import wolframalpha # Wolfram Alpha API, for powerful computations
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WolfRamAlpha(query):
    print(f"Query beingsent :{query}")
    apikey = "8R4E8T-6YQ25X9R2A"
    requester = wolframalpha.Client(apikey) #creates a new client that can interact with the wolframalpha api using provided apikey.
    requested = requester.query(query) #this line sends the query to the wolframalpha api 
     #print(requested)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query) # Converts the query to a string
    Term = Term.replace("eve","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")