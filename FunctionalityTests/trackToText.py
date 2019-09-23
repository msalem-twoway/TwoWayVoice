# This script contains functions to simulate the different key presses that the Central Station makes
# when using two-way voice with a panel
import threading
import time

from micToText import micToText
from playAudio import playAudio
from harvardSentences import hs
from random import randrange

FILE = 0
TEXT = 1

# This function test the functionality when a Central Station(CS) has pressed the '3' button on their phone
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
def trackToText(cs_mic,pnl_mic,cs_speaker,pnl_speaker):

	track = randrange(4) #generate a random number to select which audio file to test with
	# track = 3

	# Run the micToText function with a flag so that we can import the speechrecognition module
	# before spinning up a thread. This allows us to prevent a race condition that would
	# periodically crash the program
	micToText(2,True)

	#Can the CS hear the panel?
	pnl_audio_thread=threading.Thread(target=playAudio, args=(pnl_speaker,hs[track][FILE]))
	pnl_audio_thread.start()
	transcription=micToText(cs_mic,False)
	while pnl_audio_thread.isAlive():
		time.sleep(0.1)
	if(str(transcription).lower()==str(hs[track][TEXT]).lower()):
		print("Pass! Call was understood")

	track = randrange(4) #generate a random number to select which audio file to test with

	pnl_audio_thread=threading.Thread(target=playAudio, args=(pnl_speaker,hs[track][FILE]))
	pnl_audio_thread.start()
	transcription=micToText(cs_mic,False)
	while pnl_audio_thread.isAlive():
		time.sleep(0.1)
	if(str(transcription).lower()==str(hs[track][TEXT]).lower()):
		print("Pass! Call was understood")

	track = randrange(4) #generate a random number to select which audio file to test with

	pnl_audio_thread=threading.Thread(target=playAudio, args=(pnl_speaker,hs[track][FILE]))
	pnl_audio_thread.start()
	transcription=micToText(cs_mic,False)
	while pnl_audio_thread.isAlive():
		time.sleep(0.1)
	if(str(transcription).lower()==str(hs[track][TEXT]).lower()):
		print("Pass! Call was understood")
	track = randrange(4) #generate a random number to select which audio file to test with

	pnl_audio_thread=threading.Thread(target=playAudio, args=(pnl_speaker,hs[track][FILE]))
	pnl_audio_thread.start()
	transcription=micToText(cs_mic,False)
	while pnl_audio_thread.isAlive():
		time.sleep(0.1)
	if(str(transcription).lower()==str(hs[track][TEXT]).lower()):
		print("Pass! Call was understood")
	track = randrange(4) #generate a random number to select which audio file to test with

	pnl_audio_thread=threading.Thread(target=playAudio, args=(pnl_speaker,hs[track][FILE]))
	pnl_audio_thread.start()
	transcription=micToText(cs_mic,False)
	while pnl_audio_thread.isAlive():
		time.sleep(0.1)
	if(str(transcription).lower()==str(hs[track][TEXT]).lower()):
		print("Pass! Call was understood")
