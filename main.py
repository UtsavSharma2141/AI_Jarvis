import datetime
import os

import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    #speak("hello my name is jarvis, how can i help you today?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("how can i help you?")
        print("Working on your request")
        r.pause_threshold = 1;
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        speak("Please Say it again..")
        return "None"
    return query


if __name__ == '__main__':
    #wishMe()
    while True:
        query = takeCommand().lower()
        # Executing different tasks
        if 'wikipedia' in query:
            speak("searching on wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            webbrowser.get('chrome')

        elif 'open google' in query:
            webbrowser.open("google.com")
            webbrowser.get('chrome')

        elif 'play music' in query:
            webbrowser.open("https://music.youtube.com/")
            webbrowser.get('chrome')


