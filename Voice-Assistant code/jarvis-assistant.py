import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[13].id)

def speak(text):
  print('[Jarvis] : ' +text)
  engine.say(text)
  engine.runAndWait()

def wish_me():
  hour = int(datetime.datetime.now().hour)
  greeting = ''

  if hour>=0 and hour<12:
    greeting = 'Good morning!'
  elif hour>=12 and hour<18:
    greeting = 'Good afternoon!'
  else:
    greeting = 'Good evening!'

  speak(greeting + ' I am Jarvis, How can I help you today?')

def takeCommand():
  #It takes microphone input from the user and returns string output
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

  try:
    print("Recognizing...")    
    command = r.recognize_google(audio, language='en-in')
    print('[Me]:' +command)

  except Exception as e:
    # print(e)    
    return "None"
  return command

# script starts here

wish_me()
while True:
# if 1:
  command = takeCommand().lower()

  # Logic for executing tasks based on command
  command = command.replace('jarvis', '')

  if 'wikipedia' in command:
    speak('Searching Wikipedia...')
    command = command.replace("wikipedia", "")
    command = command.replace("search", "")
    command = command.replace("for", "")
    results = wikipedia.summary(command, sentences=1)
    speak('According to wikipedia, ' +results)

  elif 'open youtube' in command:
    speak('Opening Youtube')
    webbrowser.open("https://youtube.com")

  elif 'open google' in command:
    speak('Opening Google')
    webbrowser.open("https://google.com")

  elif 'open stack overflow' in command:
    speak('Opening StackOverflow')
    webbrowser.open("https://stackoverflow.com")

  elif 'what' in command and 'time' in command:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak('Sir, The time is ' +strTime)

  elif 'meaning of life' in command:
    speak('Sir, the meaning of life is 42.')
  
  elif 'how are you' in command:
    speak('I am doing jolly good, sir.')

  elif 'bye' or 'thank you' in command:
    speak('Goodbye, Have a nice day!')

  else:
    speak('I didn\'t quiet catch you sir. Can you please try that again?')
    


