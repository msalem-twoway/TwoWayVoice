# This test will run through each harvard sentence i times and output to a selected .txt file
# The pass rate and what the recognizer heard if it was wrong

import threading
import time
# import speech_recognition as sr


from micToText import micToText
from playAudio import playAudio
from harvardsentences import hs


FILE = 0
TEXT = 1

# r = sr.Recognizer()
# # Selecting Mics
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

# Run the micToText function with a flag so that we can import the speechrecognition module
# before spinning up a thread. This allows us to prevent a race condition that would
# periodically crash the program
micToText(2,True)

out = open("results3.txt","a")

for track in range(22):
	success=0
	failedList = []
	correctString=str(hs[track][TEXT]).lower()
	clipName=str(hs[track][FILE])
	for i in range(15):
		#Can the CS hear the panel?
		pnl_audio_thread=threading.Thread(target=playAudio, args=(4,hs[track][FILE]))
		pnl_audio_thread.start()
		transcription=micToText(2,False) #transcription holds the string that was transcribed from the audio clip
		while pnl_audio_thread.isAlive(): #make sure the thread has finished before moving on to avoid two audio clips playing at the same time
			time.sleep(0.1)
		if (str(transcription).lower() == str(hs[track][TEXT]).lower()):
			success += 1
		else:
			failedList.append(str(transcription))
	out.write("%s/15 Passed for string - %s - Clip: %s \n Failed cases: \n" % (success, correctString, clipName))
	out.write("\n".join(failedList))
	out.write("\n")

