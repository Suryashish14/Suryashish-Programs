import pyttsx3
import datetime
import wikipedia
import webbrowser
import calculator as calc
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',110)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!!')
    elif hour>=12 and hour<17:
        speak('Good Afternoon!!')
    else:
        speak('Good Evening!!')
    speak('I am your  Dekstop  Assistant  How  May  I  Help  You')
wish()
def command(str):
    speak(' Please Enter Your Command!!')
    str=input('Please Enter Your Command-->')
    return str.lower()
while True:
    task=command(str)
    if 'open youtube'in task:
        webbrowser.open('youtube.com')
        speak('Opening Youtube')
        print('Opening Youtube....')
    elif 'open google'in task:
        webbrowser.open('google.com')
        speak('Opening google')
        print('Opening Google....')
    elif 'open gmail'in task:
        webbrowser.open('gmail.com')
        speak('Opening Gmail')
        print('Opening Gmail.....')
    elif 'exit' in task:
        print('\t\t\t\t\t\t\tTHANK YOU')
        speak('Thank You For Using ACE Dekstop Assistant!!')
        break
    elif 'open calculator'in task:
        speak('Enter The First Number!!')
        com1=float(input('Enter Your First Number-->'))
        speak('Enter The Second Number!!')
        com2=float(input('Enter Your Second Number-->'))
        speak('What will you like to do.?? ADD,SUBSTRACT,MULTIPLY or DIVISION.?')
        inst=input('What will you like to do.?? ADD,SUBSTRACT,MULTIPLY or DIVISION.?-->')
        speak('here is your answer')
        if inst.lower()=='add':
            calc.addition(com1,com2)
        elif inst.lower()=='substract':
            calc.substraction(com1,com2)
        elif inst.lower()=='multiply':
            calc.multiplication(com1,com2)
        elif inst.lower()=='division':
            calc.division(com1,com2)
    elif 'wikipedia'in task:
        print('Searching Wikipedia...')
        speak('Searching Wikipedia')
        task= task.replace("wikipedia", "")
        ans= wikipedia.summary(task, sentences=3)
        speak("According to Wikipedia ")
        print(ans)
        speak(ans)
    elif 'time' in task:
        Time = datetime.datetime.now().strftime("%H:%M:%S")    
        print(f'The Time is:{Time}')
        speak(f"The time is:{Time}")
    elif 'open code' in task:
        path="C:\\Users\\Home\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        print('Opening VS Code.....')
        speak('Opening VS Code')
        os.startfile(path)
    elif 'open whatsapp'in task:
        webbrowser.open('web.whatsapp.com')
        print('Openining Whatsapp')
        speak('Openining Whatsapp')
    elif 'open word'in task:
        path='C:\\ACE\\Sample\\Sample1.doc'
        print('Opening MS Word....')
        speak('Opening MS Word')
        os.startfile(path)
    elif 'open powerpoint' or 'open ppt' in  task:
        path='C:\\ACE\\Sample\\Sample1.pptx'
        print('Opening MS Powerpoint....')
        speak('Opening MS Powerpoint')
        os.startfile(path)
    elif 'open access'in task:
        path='C:\\ACE\\Sample\\Sample1.accdb'
        print('Opening MS Access....')
        speak('Opening MS Access')
        os.startfile(path)
    elif 'open excel' in task:
        path='C:\\ACE\\Sample\\Sample1.xls'
        print('Opening MS Excel.....')
        speak('Opening MS Excel')
        os.startfile(path)
    elif 'open notepad'in task:
        path='C:\\ACE\\Sample\\Sample1.txt'
        print("Opening Notepad....")
        speak("Opening Notepad")
        os.startfile(path)
    # TEMP END       
        
        
