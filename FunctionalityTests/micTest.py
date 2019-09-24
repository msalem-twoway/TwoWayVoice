import speech_recognition as sr

r = sr.Recognizer()
speech = sr.Microphone(device_index=2,sample_rate=44100,chunk_size=4096)

with speech as source:
    print("say something:")
    audio = r.adjust_for_ambient_noise(source,duration=1)
    audio = r.listen(source)
try:
    #recog = r.recognize_wit(audio, key = "6Y4KLO4YTWDQSYQXGONPHAVB3IRSWFRN")
    with open("mic-results.wav","wb") as f:
        f.write(audio.get_wav_data())
    #print("You said: " + recog)
except sr.UnknownValueError:
    print("could not understand audio")
except sr.RequestError as e:
    print("Could not request results ; {0}".format(e))
