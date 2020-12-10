import pyttsx3


# pip3 install pyttsx3
def speak(text):
    pyttsx3.speak(text)


speak('What is your name?')
name = input('Please enter your name: ')

speak('Hello' + name + 'Hurry up. I am hungry!')
