import pymysql
import speech_recognition as sr
from tkinter import *
import pyttsx3
import pyaudio
goku = pyttsx3.init()
goku.setProperty('rate', 150)
goku.setProperty('volume', 9)
marvel =Tk()
def ts():
    global eee
    for i in range(100):
        v = StringVar()
        eee = Entry(marvel, textvariable=v,width=60)
        eee.grid(row=2, column=0)
        bt = Button(marvel, text="send", command=ts1).grid(row=2, column=3)
def ts1():
    global eee
    a = eee.get()
    eee.delete(0, 'end')
    db = pymysql.connect(host='localhost', user='carol', password='danvers', db='aaj')
    cur = db.cursor()
    sq = ("""select ans from robo where ques like""" + "'" + "%" + a + "%" + "'")
    cur.execute(sq)
    dat = cur.fetchone()
    a = str(dat).strip('[]()'',')
    goku.say(a)
    print("robo:",a)
    goku.runAndWait()
def ss():
    r = sr.Recognizer()
    chunk_size = 2048
    sample_rate = 48000
    mn="bcm2835 ALSA: IEC958/HDMI (hw:0,1)"
    mic_list = sr.Microphone.list_microphone_names()
  
    for i, microphone_name in enumerate(mic_list): 
        if microphone_name == mn: 
            de = i
    with sr.Microphone(sample_rate=48000,chunk_size=512) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        a = r.recognize_google(audio)
        print("you:",a)
        a=a.lower()
        db = pymysql.connect(host='localhost', user='carol', password='danvers', db='aaj')
        cur = db.cursor()
        sq = ("""select ans from robo where ques like""" + "'" + "%" + a + "%" + "'")
        cur.execute(sq)
        dat = cur.fetchone()
        a = str(dat).strip('[]()'',')
        print(a)
        goku.say(a)
        goku.runAndWait()
button=Button(marvel,text="text input",command=ts,width=40,height=5).grid(row=10,column=40)
but1=Button(marvel,text="speech input",command=ss,width=40,height=5).grid(row=40,column=40)
mainloop()
