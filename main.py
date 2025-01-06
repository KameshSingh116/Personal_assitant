#Radhe Radhe 
import speech_recognition as sr
import pyaudio as pa
import webbrowser as wb
import  pyttsx3 
import setuptools as st



recognixer=sr.Recognizer() #Obatain the speech rrecognition functionality ability
engine=pyttsx3.init() #To initialize the pyttsx3 module

def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__=="__main__":
    speak("Initializing Jarvis")
    while True:
     #Listen for the wake word "Mickey"
    #Obtain audio from microphone

     r=sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         audio=r.listen(source)
         
         
         command=r.recognize_sphinx(audio)
         print(command)

    #
     