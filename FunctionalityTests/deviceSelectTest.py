# This test will let you pick a speaker and microphone for noth CS and Panel sides and then test them

import speech_recognition as sr
import threading
import time
import sys

from micToText import micToText
from playAudio import playAudio

r = sr.Recognizer()

#Selecting Mics
# mic_list = sr.Microphone.list_microphone_names()
# print('\n'.join('{}: {}'.format(*k) for k in enumerate(mic_list)))
# print("Please select the number of the microphone you would like to use for the CS:")
# cs_mic=int(input())
# print("Please select the number of the microphone you would like to use for the Panel:")
# pnl_mic=int(input())
# print("Please select the number of the speaker you would like to use for the CS:")
# cs_speaker=int(input())
# print("Please select the number of the speaker you would like to use for the Panel:")
# pnl_speaker=int(input())

micToText(2,True)

audio_thread=threading.Thread(target=playAudio, args=(2,sys.argv[1]))
audio_thread.start()
micToText(2,False)
while audio_thread.isAlive():
	time.sleep(0.1)

# #CS mic test

# with cs_mic as source:
#     print("Speak into the CS mic")
#     audio = r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
# try:
#     recog = r.recognize_wit(audio, key = "6Y4KLO4YTWDQSYQXGONPHAVB3IRSWFRN")
#     print("You said: " + recog)
# except sr.UnknownValueError:
#     print("could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results ; {0}".format(e))

# #Panel mic test

# with pnl_mic as source:
#     print("Speak into the CS mic")
#     audio = r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
# try:
#     recog = r.recognize_wit(audio, key = "6Y4KLO4YTWDQSYQXGONPHAVB3IRSWFRN")
#     print("You said: " + recog)
# except sr.UnknownValueError:
#     print("could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results ; {0}".format(e))



