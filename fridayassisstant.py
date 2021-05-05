import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import requests
import wikipedia
import webbrowser as wb
import easygui
from youtube_search import YoutubeSearch
from tkinter import filedialog
from tkinter import messagebox as msg
import os
import pyautogui
import psutil
import pyjokes
import sys
from selenium import webdriver
import time
import glob
import json
import pytesseract
from PIL import Image
from translate import Translator
from test2 import * 
from selenium.webdriver.chrome.options import Options
import math
from PyDictionary import PyDictionary as dictionary
import PyCurrency_Converter as cur
from textblob import TextBlob
import cv2
import winsound

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

BLYNK_AUTH = 'YAZcukJARbe37k5oIeJnfEnH6LRCGeAd'
BLYNK_URL = 'http://blynk-cloud.com/'
put_header={"Content-Type": "application/json"}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def asktime():
    asktime = datetime.datetime.now().strftime("%I:%M:%S")
    speak(asktime)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back!")
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("good morning sailesh!")
    elif hour >=12 and hour <18:
        speak("good afternoon sailesh!")
    elif hour >=18 and hour <24:
        speak("good evening sailesh!")
    else:
        speak("good night sailesh!")

    speak("friday is with you sir!")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
          
    
    except Exception as e:
        print(e)
        speak("say that again please...")

        return "None"
    return query
    


def takecommand1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
         print(e)
         return "None"
    return query

def screenshot():
        name = "screenshot"
        name = '{}.png'.format(name)
        img = pyautogui.screenshot(name)

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def convert():
    speak("which image do you want?")
    path = takecommand()
    os.chdir("C:\\Users\\DELL\\Pictures")   
    for file in glob.glob(path+"*.jpg"):
        text = pytesseract.image_to_string(file)
        print(text)
        speak(text)

def file_name():
  read=easygui.fileopenbox()
  return read

def file_open():
    file=file_name()
    try:
     os.startfile(file)
     msg.showinfo('success',"File opened !")
    except Exception as e:
        print(e)
        msg.showinfo('error',"File invalid !")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def sendEmail(to,subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sailesh67876@gmail.com', 'sailesh12321')
    server.sendmail('sailesh67876@gmail.com', to, content)
    server.close()

def stop_listening():
    speak("ok sir waiting for commands")
    i=1
    print(i)
    while i==1:
        query=takecommand1()
        if ("start listening" or  "hey Friday")in query:
            speak('resuming operations')
            break
        else:
            continue

def jokes():
    speak(pyjokes.get_joke()) 

def securecam():

    cam = cv2.VideoCapture(0)

    while cam.isOpened():
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1 , frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray , (5 , 5), 0)
        _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame1, contours, -1,(0,255,0), 2)
        for c in contours:
            if cv2.contourArea(c) < 4000:
                continue
            x,y,h,w = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x,y) , (x+w , y+h) , (0,255,0) , 3)
            winsound.Beep(1000 , 500)

            if cv2.waitKey(10) == ord ('`'):
                break

        cv2.imshow("friday's vision" , frame1)   

def lighton():
    val = 0
    put_body = json.dumps([val])
    r = requests.put(BLYNK_URL+BLYNK_AUTH+'/update/D16', data=put_body, headers=put_header)

def lightoff():
    val = 1
    put_body = json.dumps([val])
    r = requests.put(BLYNK_URL+BLYNK_AUTH+'/update/D16', data=put_body, headers=put_header)

def fanon():
    val = 0
    put_body = json.dumps([val])
    r = requests.put(BLYNK_URL+BLYNK_AUTH+'/update/D05', data=put_body, headers=put_header)

def fanoff():
    val = 1
    put_body = json.dumps([val])
    r = requests.put(BLYNK_URL+BLYNK_AUTH+'/update/D05', data=put_body, headers=put_header)

def computeron():
    val = 0
    put_body = json.dumps([val])
    r = requests.put(BLYNK_URL+BLYNK_AUTH+'/update/D4', data=put_body, headers=put_header)

def computeroff():
    val = 1
    put_body = json.dumps([val])
    r = requests.put(BLYNK_URL+BLYNK_AUTH+'/update/D4', data=put_body, headers=put_header)

def summaon():
    val = 0
    put_body = json.dumps([val])
    r = requests.put(BLYNK_URL+BLYNK_AUTH+'/update/D0', data=put_body, headers=put_header)

def summaoff():
    val = 1
    put_body = json.dumps([val])
    r = requests.put(BLYNK_URL+BLYNK_AUTH+'/update/D0', data=put_body, headers=put_header)


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'time' in query:
           asktime()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'send email' in query:
            try:
                speak("what is the subject?")
                subject = takecommand()
                speak("what should i say?")
                content = takecommand()
                speak("to whom i want to send?")
                to = takecommand()
                sendEmail(to,subject,content)
                speak("sir the Email has successfully sent!")
            except Exception as e:
                print(e)
                speak("unable to send the Email sir")

        elif 'search in chrome' in query:
            speak("what should i search for?")
            driver = webdriver.Chrome("C:\\Users\DELL\\chromedriver_win32\\chromedriver.exe")
            search = takecommand().lower()
            search = search.replace(' ','+')
            driver.get("https://www.google.com/search?q="+search)

        elif 'search in youtube' in query:
            speak("what should i search for?")
            search = takecommand()
            pywhatkit.playonyt(search)

        elif 'logout' in query:
            os.system("shutdown -1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' or 'shut down' or 'Shutdown' in query:
            os.system("shutdown /s /t 1")

        
        elif 'play music' in query:
            speak("which song do yo want?")
            paadal = takecommand()
            os.chdir("C:\\Users\\DELL\\Music")
            for file in glob.glob(paadal+"*.mp3"):
                print(file)
            paadal_dir = "C:\\Users\\DELL\\Music"
            paatu = os.listdir(paadal_dir)
            os.startfile(os.path.join(paadal_dir, file))
            stop_listening()

        elif 'play movie' in query:
            speak("which movie do yo want?")
            file=file_open()
            os.startfile(file)
            stop_listening()


        elif 'switch on the light' or 'turn on the light' or 'lights on'  in query:
            speak("switching on the lights")
            lighton()

        elif 'switch off the light' or 'turn off the light' or 'lights off'  in query:
            speak("switching off the lights")
            lightoff()

        elif 'switch on the fan' or 'turn on the fan' or 'fan on'  in query:
            speak("switching on the fan")
            fanon()

        elif 'switch off the fan' or 'turn off the fan' or 'fan off'  in query:
            speak("switching off the fan")
            fanoff()

        elif 'switch on the computer'or 'turn on the computer' or 'computer off'  in query:
            speak("power on the computer")
            computeron()

        elif 'switch off the computer'or 'turn off the computer' or 'computer off'  in query:
            speak("power off the computer")
            computeroff()

        elif 'open Atom' in query:
            app = "C:\\Users\\DELL\\AppData\\Local\\atom\\atom.exe"
            os.startfile(os.path.join(app))

        elif 'remember that' in query:
            speak("what should i want to remember sir?")
            data = takecommand()
            speak("you said me to remember that "+data)
            remember = open("data.txt",'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open("data.txt", 'r')
            speak("you said me to remember that "+remember.read())

        elif 'sleep' or 'stop listening' or 'wait' in query:
            stop_listening()

        elif 'screenshot' in query:
            screenshot()
            speak("done!")

        elif 'cpu' in query:
            cpu()

        elif 'security' or 'secure mode' or 'protected' in query:
            securecam()

        elif 'joke' in query:
            jokes()

        elif 'translate' or 'translator'or 'Translate' in query:
            speak("to which language i want to translate?")
            eluthu = takecommand()
            translator= Translator(to_lang = eluthu)
            speak("which sentence i want to translate?")
            eluthu2 = takecommand()
            translation = translator.translate(eluthu2)
            print (translation)
            speak (translation)

        elif 'what is your name' or 'name' or 'Name' in query:
            speak("I am friday...your personalized AI assisstant")

        elif 'what can you do for me' or 'do for me' or 'what can you do' in query:
            speak("I can do anything for you sir...like basic commands, opening files, and controlling your PC sir")

        elif 'thank you' or 'thankyou' or 'ok' or 'okay' in query:
            speak("its my pleasure sir")

        if 'hey' or 'hi' or 'hello' or 'friday' in query:
            speak("hello sir...i am listening...")

        elif 'How is it going?' or 'how is it going' or 'how are you' in query:
            speak("Great"),("going good!"),("could be better")


        elif 'how is the weather' or 'weather' or 'weather updates' in query:

            api_key = "f897ab2ccc8605720500a249298f76db"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("which city do you want sir")
            city_name = takecommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            y = x["main"] 
            current_temperature = y["temp"]
            current_pressure = y["pressure"] 
            current_humidiy = y["humidity"]  
            z = x["weather"] 
            weather_description = z[0]["description"] 
            speak(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description))

        elif 'ocr'or 'perform ocr' or 'extract' in query:
            convert()

        elif 'search lyrics' or 'lyrics' or 'find lyrics' in query:
            print("Welcome to the Musixmatch API explorer!")
            speak("Welcome to the Musixmatch API explorer!")
            print()
            try:
                print("Whats's the name of the artist?")
                speak("Whats's the name of the artist?")
                hear = takecommand()
                artist_name = (hear)
                print("What's the name of the track?")
                speak("What's the name of the track?")
                hear1 = takecommand()
                track_name = (hear1)
                api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
                request = requests.get(api_call)
                data = request.json()
                data = data['message']['body']
                print("API Call: " + api_call)
                print()
                speak("here it is!") 
                print(data['lyrics']['lyrics_body'])
     
            except Exception as e:
                print("song not found")
                speak("song not found")
                speak("searching in browser...")
                driver = webdriver.Chrome("C:\\Users\\DELL\\chromedriver_win32 (1)\\chromedriver.exe")
                driver.get("https://genius.com/search?q="+hear1)
                time.sleep(10)
                driver.find_element_by_css_selector("a.mini_card").click()
                

        elif 'remind' in query :
            speak("What shall I remind you about?")
            text = takecommand()
            speak("In how many minutes?")
            ethavathu = takecommand()
            local_a = int(ethavathu)
            local_a = ((local_a) * 10)
            x = int(local_a)
            time.sleep(x)
            print(text)
            speak(text)

        elif 'meaning' in query:
            speak("say me a word")
            word = takecommand()
            print(dictionary.meaning(word))
            speak(dictionary.meaning(word))
        

        elif 'go offline' in query:
            speak("friday at your service sir...have a good day")
            sys.exit(0)

        elif 'none' in query:
            takecommand()

        else:

         speak("I don't know....would you like to search further??")
         opinion = takecommand()
         if 'yes' or 'sure' or 'definitely' in query:

            speak("cannot find.... searching in google")
            driver = webdriver.Chrome("C:\\Users\\DELL\\chromedriver_win32\\chromedriver.exe")
            search = query
            search = search.replace(' ','+')
            driver.get("https://www.google.com/search?q="+search)
            stop_listening()
             
   

            