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
    speak("Hey! Nice to meet you sir")
    speak("How was you day !")


