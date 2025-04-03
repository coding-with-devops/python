import pyttsx3
engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate

engine.say("Welcome World and My Name is Aarvi")
engine.runAndWait()