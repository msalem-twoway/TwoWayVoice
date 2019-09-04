import speech_recognition as sr

r = sr.Recognizer()
speech = sr.Microphone()
word = "hello"

with speech as source:
    print("say something!!….")
    audio = r.adjust_for_ambient_noise(source)
    audio = r.listen(source, phrase_time_limit=5)
try:
    recog = r.recognize_wit(audio, key = "6Y4KLO4YTWDQSYQXGONPHAVB3IRSWFRN")
except sr.UnknownValueError:
    print("could not understand audio")
except sr.RequestError as e:
    print("Could not request results ; {0}".format(e))

if(recog.lower() == word.lower()):
	print("Match!")
else:
	print("Fail :( you said "+recog)