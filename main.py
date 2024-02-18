import pyttsx3

text = input('What do you want to be said: ')
speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()

