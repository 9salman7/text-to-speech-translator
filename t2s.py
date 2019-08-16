# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
from playsound import playsound
from googletrans import Translator
import os 
   
language = 'en'

translator=Translator()

inputText=input("Enter text to translate to English\n");

transText=translator.translate(inputText).text
  
myobj = gTTS(text=transText, lang=language, slow=False) 

myobj.save("welcome.mp3") 
  
playsound('welcome.mp3')