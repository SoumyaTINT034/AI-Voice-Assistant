import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyttsx3
import time
import os


def SpeechToText():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recongnizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understanding...")


def TextToSpeech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':

 while True:
    data1 = SpeechToText().lower()
    if "who made you" in data1:
        owner = "S D B has created me, many thanks to him"
        TextToSpeech(owner)

    elif "old" in data1:
        age = "I am two years old"
        TextToSpeech(age)

    elif "name" in data1:
        name = "My name is laser, welcome to virtual world"
        TextToSpeech(name)

    elif "language" in data1:
        language = "I am programmed to speak in English, but I love bengali, NOMOSKAR "
        TextToSpeech(language)

    elif "live" in data1:
        place = "I live in Kolkata, I am Assistant of S D B"
        TextToSpeech(place)

    elif "time" in data1:
        time = datetime.datetime.now().strftime("%I%M%p")
        x = "The time is now"
        TextToSpeech(x + time)

    elif "hello" in data1:
        greet = "Hello Dude, How are you"
        TextToSpeech(greet)


    elif "kali song" in data1:
        add = "C:\\Users\\user\\Music"
        listsong = os.listdir(add)
        print(listsong)
        os.startfile(os.path.join(add, listsong[2]))
    elif "ganesh song" in data1:
        add = "C:\\Users\\user\\Music"
        listsong = os.listdir(add)
        print(listsong)
        os.startfile(os.path.join(add, listsong[0]))

    elif "bye" in data1:
        TextToSpeech("Bye friend, thanks for using me! see you soon")
        break

    # time.sleep(1)
