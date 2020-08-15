# Author : Vishwajeet Dabholkar


import speech_recognition as sr
from playsound import playsound
import googletrans
from googletrans import Translator
#print(googletrans.LANGUAGES)

r = sr.Recognizer()
translator = Translator()
# # open the file
# with sr.AudioFile(filename) as source:
    # # listen for the data (load audio to memory)
    # audio_data = r.record(source)
    # # recognize (convert from speech to text)
    # text = r.recognize_google(audio_data)
    # print(text)
    
with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("Speak:")
    audio_data = r.record(source, duration= 5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data,language='en')
    result = translator.translate(text,src='en', dest='mr')
    print(text)
    print(result.text)