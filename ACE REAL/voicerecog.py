import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print('Listening......')
    audio=r.listen(source)
    try:
        print('Recognitising.....')
        text=r.recognize_google(audio,language='en-in')
        print('You Said:',text)
    except:
        print('Sorry Could Not hear Your Properly!')
