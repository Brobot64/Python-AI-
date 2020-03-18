import pyttsx3 #pip install pyttsx3
#import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys
import urllib.request, json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Brobot Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output
    print("Waiting...")
    r = input(str(""))
    audio = r
    
    try:
        print("Processing...")    
        query = audio
        print(f"User said: {query}\n")

    except exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'your password')
    server.sendmail('email', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
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

        elif 'search' in query:
            #speak('Enter what you want me to search')
            #search = input()
            url = 'str(search)'
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.get(chrome_path).open(url)
        
        elif 'open music' in query:
            music_dir = "C:\\Program Files\\Windows Media Player\\wmplayer.exe"
            os.startfile(music_dir)
            speak('Opening music')
        
        elif 'open video' in query:
            vid_dir = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(vid_dir)
            speak('Opening Video player')

        elif 'play music' in query:
            music_dir = "C:\\Users\\Ibrahim\\Music\\Playlists\\mine3.wpl"
            os.startfile(music_dir)
            speak('Preparing music')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "http://localhost:8888/edit/Documents/Ibrahim Proj/project4.py"
            os.startfile(codePath)
        elif 'open chrome' in query:
            browserPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(browserPath)
            
        elif 'show me direction' in query:
            #Google MapsDdirections API endpoint
            endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
            api_key = 'AIzaSyCLNO5mol_LjqDuOkTKLBke4Q9de-6GVy4'
            #Asks the user to input Where they are and where they want to go.
            origin = input('Where are you?: ').replace(' ','+')
            destination = input('Where do you want to go?: ').replace(' ','+')
            #Building the URL for the request
            nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
            request = endpoint + nav_request
            #Sends the request and reads the response.
            response = urllib.request.urlopen(request).read()
            directions = response
            #Loads response as JSON
            print(directions)
            speak(directions)

        elif 'email to ibrahim' in query:
            try:
                speak("What should I say?")
                print("Enter the content: ")
                content = takeCommand()
                r = input("Enter the email address")
                to = str(r)    
                sendEmail(to, content)
                speak("Email has been sent!")
            except:# exception as e:
                #print(e)
                speak("Sorry my friend Ibrahim. I am not able to send this email")    
        
        elif 'exit' in query:
            exit()
