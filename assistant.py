import speech_recognition as sr
import pyttsx3

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
        talk("playing")
        print("playing")
        
run_karen()