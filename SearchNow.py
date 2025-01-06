import pyttsx3
import speech_recognition 
import pywhatkit #sending whatsapp msgs.
import wikipedia
import webbrowser



def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening ma'am........")
        r.pause_threshold = 1 
        r.energy_threshold = 300    #voice cancellation

        audio = r.listen(source,0,4)     #4 second wait krega and will move forward

    try:
        print("understanding........")
        query = r.recognize_google(audio,language='en-in')
        print(f"you said : {query}\n")
    except Exception as e:
        print("please say that again")
        return "none"
    return query


query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("eve"," ")
        query = query.replace("google search"," ")
        query = query.replace("google"," ")
        query = query.replace("on"," ")
        speak("this is what i found on google")


        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("no speakable output found")

def searchYoutube(query):
    if "youtube" in query:
        speak("this is what i found for you search")
        query = query.replace("youtube"," ")
        query = query.replace("eve"," ")
        query = query.replace("play"," ")
        query = query.replace("on"," ")

        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("done ma'am")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)
