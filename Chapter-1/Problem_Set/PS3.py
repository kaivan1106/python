#go to https://pypi.org/project/pyttsx3/ so that you will get the command to install a module and code which will speak
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text") #whatever you will write, system will speak
engine.runAndWait()