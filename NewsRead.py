import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=b73abcab7a484c76a0c311e1ad32f02f",
        "entertainment": "https://newsapi.org/v2/top-headlines?category=entertainment&apiKey=b73abcab7a484c76a0c311e1ad32f02f",
        "health": "https://newsapi.org/v2/top-headlines?category=health&apiKey=b73abcab7a484c76a0c311e1ad32f02f",
        "science": "https://newsapi.org/v2/top-headlines?category=science&apiKey=b73abcab7a484c76a0c311e1ad32f02f",
        "sports": "https://newsapi.org/v2/top-headlines?category=sports&apiKey=b73abcab7a484c76a0c311e1ad32f02f",
        "technology": "https://newsapi.org/v2/top-headlines?category=technology&apiKey=b73abcab7a484c76a0c311e1ad32f02f"
    }

    content = None
    url = None
   
    speak("Which field news do you want, [business], [health], [technology], [sports], [entertainment], [science]")
    print("Which field news do you want, [business], [health], [technology], [sports], [entertainment], [science]")
    field = input("Type the field of news that you want: ").lower()

    url = api_dict.get(field)
    if url is None:
        print("Invalid field. Please choose from the available options.")
        return

    print("URL was found:", url)

    news = requests.get(url).json()

    if "articles" not in news:
        print("No articles found in the response.")
        return

    articles = news["articles"]
    speak("Here is the first news.")
    
    for article in articles:
        title = article.get("title")
        if title:
           
            print(title)
            speak(title)
            news_url = article.get("url")
            if news_url:
                print(f"For more info visit: {news_url}")

            inputUser = input("[Press 1 to continue] and [Press 2 to stop]: ")
            if inputUser == "2":
                break
        
    speak("That's all")

latestnews()
