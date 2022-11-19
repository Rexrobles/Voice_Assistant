import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
try:
    with sr.Microphone() as source:
        print("listening....")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if "karen" in command:
            talk(command)
            print(command)
except:
    pass