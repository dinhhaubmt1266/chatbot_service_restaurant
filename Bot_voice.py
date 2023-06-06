from email import message
import requests 
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

bot_message = ""

mytext = "Nhà xe Kim Ngân xin kính chào quý khách!"
mytextobj = gTTS(mytext, lang='vi', slow=False)
mytextobj.save("welcome1.mp3")
sound = AudioSegment.from_mp3('welcome1.mp3')
sound.export("welcome1.wav", format='wav')
sound_wav = AudioSegment.from_wav('welcome1.wav')
play(sound_wav)

#playsound.playsound('welcome1.wav')

while bot_message != "thanks" :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak anything :")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=2)
        print("Done recording")
        try:
            message = r.recognize_google(audio, language="vi-VN")
            print("You say : {}".format(message))
        except:
            print("Sorry could not reconize your voice")

    if len(message) == 0:
        continue
    print("Sending message now ...")

    r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": message})
    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = gTTS(text=bot_message, lang="vi", slow=False)

    myobj.save("welcome.mp3")
    sound_myobj = AudioSegment.from_mp3('welcome.mp3')
    sound_myobj.export("welcome.wav", format = 'wav')
    sound_myobj_wav = AudioSegment.from_wav('welcome.wav')
    play(sound_myobj_wav)

    #playsound.playsound('welcome.mp3', True)
