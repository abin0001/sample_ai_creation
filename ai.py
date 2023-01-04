import pyttsx3
from decouple import config



engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    
    
    engine.say(text)
    engine.runAndWait()
