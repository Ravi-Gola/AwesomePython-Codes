import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir ")
    else:
        speak("good evening sir")
    speak("I am mini Ravi Robo . please tell me how may i help you")


def takecommand():
    """ this function takes your voice and convert this in string and return this string"""
    # here we take your voice through
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening......")
        r.pause_threshold=1
        r.energy_threshold= 3500
        audio = r.listen(source)
    try:
        # here we convert audio in to string
        speak("processing chal rahi hai........")
        query = r.recognize_google(audio, language='en-in')
        speak(f"you said:{query}\n")

    except Exception as e:
        print("something wrong....")
        return "none"
    return query

friendslist={"sachin":"sachin is ravi's friend he has a shop with name chetan chosmetic store near ravi's house he is chutiya person","mannu":"mannu is a younger brother of ravi"}
if __name__ == '__main__':
        wishme()
        command = takecommand().lower()
        if "wikipedia" in command:
            speak("searching in wikipedia....")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak(f"according to wikipedia...{results}\n")
        elif "open youtube" in command:
            webbrowser.open("youtube.com")
        elif "open chrome" in command:
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(chromepath)
        elif "time" in command:
            timenow = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"now is the time {timenow}")
        elif "music" or"songs" in command:
            music_dir = "F:\\nokia 5.1 plus\\my audio song\\heart touching old songs"
            songslist = os.listdir(music_dir)
            no_of_songs = len(songslist)
            song = random.randint(0, no_of_songs)
            print(songslist[song])
            play = os.startfile(os.path.join(music_dir, songslist[song]))
        elif "friends" or"friend" in command:
            speak(" sir")
            name=takecommand().lower()
            try:
                speak(friendslist[name])
            except Exception as e:
                speak("sorry sir wrong infomation try again!")

        else:
            speak("this functionalty not available now but work in progress we will provide this funtionalty you soon")





