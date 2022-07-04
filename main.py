import datetime
import pyttsx3
import speech_recognition as sr

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
    speak("hello my name is jarvis, how can i help you today?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #speak.say('Hey I am Listening..')
        print("Working on your request")
        #speak.runAndWait()
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Please Say it again..")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    takeCommand()