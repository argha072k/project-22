import pyttsx3.voice
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') 

engine.setProperty('voice', voices[1].id)
r=sr.Recognizer()

def speak(audio):

    engine.say(audio) 
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<17:
        speak("good noon")
    else:
        speak("good evening")

    speak("i am your virtual assisstant. let me know how can i help you")

def takeCommand(): 
    
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = r.listen(source)
            query = r.recognize_google(voice)
            query = query.lower()
            if 'alexa' in query:
                query = query.replace('alexa', '')
                print(query)
    except:
        pass
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()    
 

if __name__=="__main__" :
    wishme()
    while True:   
        query = takeCommand().lower()  
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to argha' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "deeparg2k07@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my dost. I am not able to send this email")    
