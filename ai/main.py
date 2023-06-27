import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import openai
import random
from config import apikey


chatstr=""

def chat(query):
    global chatstr
    openai.api_key = apikey
    chatstr+=f"Akshat: {query}\n Jarvis "
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=chatstr,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    print(response)
    speak(response["choices"][0].text)
    chatstr +=f"{response['choices'][0]['text']}" 
    return response["choices"][0].text
    if not os.path.exists("result"):
        os.mkdir("result")

    # with open(f"result/prompt- {random.randint(1, 4246284782748365364375)}", "w") as f:
    with open(f"result/{''.join(prompt.split('ai')[1:])}.txt", "w") as f:
        f.write(text)


def ai(prompt):
    openai.api_key = apikey
    text = f"Response For Prompt: {prompt} \n ********\n\n"
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    print(response["choices"][0].text)
    text += response["choices"][0].text
    if not os.path.exists("result"):
        os.mkdir("result")

    # with open(f"result/prompt- {random.randint(1, 4246284782748365364375)}", "w") as f:
    with open(f"result/{''.join(prompt.split('ai')[1:])}.txt", "w") as f:
        f.write(text)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if (hour > 0 and hour < 12):
        speak("Good Morning!")
    elif (hour >= 12 and hour < 18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("What's Up. How Can I Help You ?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        r.energy_threshold = 900
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}\n")

        except Exception as e:
            print(e)

            print("Say That Again")
            return"None"
        return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "youtube" in query:
            webbrowser.open("youtube.com")

        elif "spotify" in query:
            webbrowser.open("open.spotify.com")

        elif "discord" in query:
            webbrowser.open("discord.com")

        elif "instagram" in query:
            webbrowser.open("instagram.com")

        elif "netflix" in query:
            webbrowser.open("netflix.com")

        elif "code" in query:
           cpath = "C:\\Users\\AKSHAT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
           os.startfile(cpath)


        elif "using ai" in query:
            ai(prompt = query)

        elif "quit" in query:
            exit()
        elif "reset chat " in query:
            chatstr = ""
        else:
            print("Chat has started")
            chat(query)

