import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "karen" in command:
                command = command.replace("karen", "")
                print(command)
    except:
        pass
    return command

def run_karen():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("The Time is" + time)
    elif "search" in command:
        person = command.replace("search", "")
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif "date" in command:
        talk("Sorry, your'e not my type")
    elif "Are you single" in command:
        talk("Im in a relationship with Google")
    elif "joke" in command:
        talk(pyjokes.get_joke())
    else:
        talk("Please say the command again")
        
        
run_karen()
