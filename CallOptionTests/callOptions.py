# This script contains functions to simulate the different key presses that the Central Station makes
# when using two-way voice with a panel
import threading
import time

from micToText import micToText
from playAudio import playAudio
from harvardSentences import hs
from random import randrange

# Harvard Sentence tuple format - (File path, Transcription)
FILE = 0
TEXT = 1


# This function tests the functionality when a Central Station(CS) has pressed the '1' button on their phone
# We create a thread that plays audio from a selected harvard sentence
# and then opens the mic on the oppposite end of the call and checks for the expected behavior
# Expected behavior: The CS cannot hear the Panel but the panel can hear the CS
# Test steps:
# 1. CS phone verifies that nothing was heard
# 2. Panel mic verifies that the correct statement was heard
# INPUTS:	cs_mic - Central Station Microphone device index
#		  	pnl_mic - Panel Microphone device index
#			cs_speaker - Central Station speaker device index
#			pnl_speaker - Panel speaker device index
# OUTPUTS:	none
def keyOne(cs_mic,pnl_mic,cs_speaker,pnl_speaker):
	track = randrange(29) #generate a random number to select which audio file to test with
	# track = 3

	# Run the micToText function with a flag so that we can import the speechrecognition module
	# before spinning up a thread. This allows us to prevent a race condition that would
	# periodically crash the program
	micToText(2,True)

	#Can the CS hear the panel?
	pnl_audio_thread=threading.Thread(target=playAudio, args=(pnl_speaker,hs[4][FILE]))
	pnl_audio_thread.start()
	transcription=micToText(cs_mic,False) #transcription holds the string that was transcribed from the audio clip
	while pnl_audio_thread.isAlive(): #make sure the thread has finished before moving on to avoid two audio clips playing at the same time
		time.sleep(0.1)
	if(str(transcription).lower()==""):
		print("Pass! Nothing was detected")

	#Can the panel hear the CS?
	cs_audio_thread=threading.Thread(target=playAudio, args=(cs_speaker,hs[4][FILE]))
	cs_audio_thread.start()
	transcription=micToText(pnl_mic,False) #transcription holds the string that was transcribed from the audio clip
	while cs_audio_thread.isAlive():
		time.sleep(0.1)
	if(str(transcription).lower()==str(hs[track][TEXT]).lower()):
		print("Pass! Call was understood")
	return


# This function tests the functionality when a Central Station(CS) has pressed the '2' button on their phone
# We create a thread that plays audio from a selected harvard sentence
# and then opens the mic on the oppposite end of the call and checks for the expected behavior
# Expected behavior: The CS can hear the Panel and the panel can hear the CS
# Test steps:
# 1. CS phone verifies that the correct statement was heard
# 2. Panel mic verifies that the correct statement was heard
# INPUTS:	cs_mic - Central Station Microphone device index
#		  	pnl_mic - Panel Microphone device index
#			cs_speaker - Central Station speaker device index
#			pnl_speaker - Panel speaker device index
# OUTPUTS:	none
def keyTwo(cs_mic,pnl_mic,cs_speaker,pnl_speaker):

	track = randrange(29) #generate a random number to select which audio file to test with
	# track = 3

	# Run the micToText function with a flag so that we can import the speechrecognition module
	# before spinning up a thread. This allows us to prevent a race condition that would
	# periodically crash the program
	micToText(2,True)

	#Can the CS hear the panel?
	pnl_audio_thread=threading.Thread(target=playAudio, args=(pnl_speaker,hs[track][FILE]))
	pnl_audio_thread.start()
	transcription=micToText(cs_mic,False) #transcription holds the string that was transcribed from the audio clip
	while pnl_audio_thread.isAlive(): #make sure the thread has finished before moving on to avoid two audio clips playing at the same time
		time.sleep(0.1)
	if(str(transcription).lower()==str(hs[track][TEXT]).lower()):
		print("Pass! Call was understood")

	#Can the panel hear the CS?
	cs_audio_thread=threading.Thread(target=playAudio, args=(cs_speaker,hs[track][FILE]))
	cs_audio_thread.start()
	transcription=micToText(pnl_mic,False) #transcription holds the string that was transcribed from the audio clip
	while cs_audio_thread.isAlive():
		time.sleep(0.1)
	if(str(transcription).lower()==str(hs[track][TEXT]).lower()):
		print("Pass! Call was understood")
	return


# This function tests the functionality when a Central Station(CS) has pressed the '3' button on their phone
# We create a thread that plays audio from a selected harvard sentence
# and then opens the mic on the oppposite end of the call and checks for the expected behavior
# Expected behavior: The CS can hear the Panel but the panel cannot hear the CS
# Test steps:
# 1. CS phone verifies that the correct statement was heard
# 2. Panel mic verifies that nothing was heard
# INPUTS:	cs_mic - Central Station Microphone device index
#		  	pnl_mic - Panel Microphone device index
#			cs_speaker - Central Station speaker device index
#			pnl_speaker - Panel speaker device index
# OUTPUTS:	none
def keyThree(cs_mic,pnl_mic,cs_speaker,pnl_speaker):
	track = randrange(4) #generate a random number to select which audio file to test with
	# track = 3

	# Run the micToText function with a flag so that we can import the speechrecognition module
	# before spinning up a thread. This allows us to prevent a race condition that would
	# periodically crash the program
	micToText(2,True)

	#Can the CS hear the panel?
	pnl_audio_thread=threading.Thread(target=playAudio, args=(pnl_speaker,hs[track][FILE]))
	pnl_audio_thread.start()
	transcription=micToText(cs_mic,False) #transcription holds the string that was transcribed from the audio clip
	while pnl_audio_thread.isAlive(): 	#make sure the thread has finished before moving on to avoid two audio clips playing at the same time
		time.sleep(0.1)
	if(str(transcription).lower()==str(hs[track][TEXT]).lower()):
		print("Pass! Call was understood")

	#Can the panel hear the CS?
	cs_audio_thread=threading.Thread(target=playAudio, args=(cs_speaker,hs[track][FILE]))
	cs_audio_thread.start()
	transcription=micToText(pnl_mic,False) #transcription holds the string that was transcribed from the audio clip
	while cs_audio_thread.isAlive():
		time.sleep(0.1)
	if(str(transcription).lower()==""):
		print("Pass! Nothing was detected")
	return