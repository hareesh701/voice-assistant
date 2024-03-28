import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak('Good Morning')
    elif 12 <= hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

    speak('Hello Sir, I am Hari, your Artificial intelligence assistant. Please tell me how may I help you')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')
    except Exception as e:
        print('Say that again please...')
        return 'None'
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senders_email@gmail.com', 'senders_password')
    server.sendmail('senders_email@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=5)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('https://www.google.com')

        elif 'play music' in query:
            speak('okay boss')
            music_dir = 'music_dir_of_the_user'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is {strtime}')

        elif 'open stack overflow' in query:
            webbrowser.open('https://stackoverflow.com')

        elif 'open WhatsApp' in query:
            os.system('WhatsApp')
            response = 'Opening WhatsApp'

        elif 'open notepad' in query:
            os.system('start notepad')
            response = 'Opening Notepad'

        elif 'open free code camp' in query:
            webbrowser.open('https://www.freecodecamp.org')

        elif 'pycharm' in query:
            codepath = 'pycharm_directory_of_your_computer'
            os.startfile(codepath)

        elif 'email' in query:
            try:
                speak('what should i write in the email?')
                content = takecommand()
                to = 'receiver_email@gmail.com'
                sendemail(to, content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('Sorry, I am not able to send this email')

        elif 'exit' in query:
            speak('okay boss, please call me when you need me')
            quit()
