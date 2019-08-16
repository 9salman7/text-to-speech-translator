from gtts import gTTS #module for text to speech
from playsound import playsound #module to play audop
from googletrans import Translator #google translate api for python 
import os 
   
language = 'en' #output language

translator=Translator()

inputText=input("Enter text to translate to English\n");

transText=translator.translate(inputText).text #translated text
  
myobj = gTTS(text=transText, lang=language, slow=False) #converted text

myobj.save("speech.mp3") #save in mp3
  
playsound('speech.mp3') #play mp3 file
