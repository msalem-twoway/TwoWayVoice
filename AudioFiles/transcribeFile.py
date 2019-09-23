import speech_recognition as sr

r = sr.Recognizer()
file = sr.AudioFile('..\AudioFiles\harvard1_5sec.wav')

with file as source:
    audio = r.record(source, duration=4.0)
try:
    recog = r.recognize_wit(audio, key = "6Y4KLO4YTWDQSYQXGONPHAVB3IRSWFRN")
    print("You said: " + recog)
except sr.UnknownValueError:
    print("could not understand audio")
except sr.RequestError as e:
    print("Could not request results ; {0}".format(e))

