import speech_recognition as sr

# This function uses the speech_recognition library and wit.ai's speech processing
# to transcribe what is heard through the microphone
# Expected behavior: A microphone will be selected based on the index and will attempts
# to transcribe any sound that is heard or timeout after 5 seconds of no activity
# INPUTS:	index - the deivce index to set the microphone to listen on
#			flag - set to true if this is the initialization call
# OUTPUTS:	returns the transcribed text that is picked up from the microphone
def micToText(index,flag):

	r = sr.Recognizer()
	r.pause_threshold=0.5 #Stop listening after 0.5 seconds of no activity
	timeout=False
	mic = sr.Microphone(device_index=index) #set microphonse to the correct index
	if flag: #for intialization only
		return

	with mic as source:
	    print("adjusting levels...")
	    audio = r.adjust_for_ambient_noise(source,duration=2) #adjust for background noise for 2 seconds
	    print("Speak into the CS mic:")
	    try:
	    	audio = r.listen(source,timeout=5) #start listening on the mic, timeout if nothing is heard after 5 seconds
	    except sr.WaitTimeoutError: #catch the timeout exception and record that we timed out
	    	timeout=True;
	if not timeout:
		try:
			print("Processing...")
			#wit_transcribed = r.recognize_wit(audio, key = "6Y4KLO4YTWDQSYQXGONPHAVB3IRSWFRN") #call wit.ai withour unique key to process what was ehard on the mic
			# transcribed = r.recognize_azure(audio_data = audio, key = "b4854ced69f44e54b9b2f2274834bf9c") #call azure with our unique key to process what was heard on the mic
			google_transcribed = r.recognize_google(audio) #call google speech services to process what was heard on the mic
			#hound_transcribed = r.recognize_houndify(audio, client_id = "5knqDZcc_eDuWTzLMLnGrg==", client_key = "Tbm-IGUR9dtyAEEfKD_dEYXppilZnCfruCLHt37Vf65j7nVDt1YCUvRSNV9wfecWxeCfGhgh07YiXbnJetsOfA==")
			#print("Wit heard: " + wit_transcribed) #print what was heard by wit.ai
			print(google_transcribed) #print what was heard by google
			#print("Houndify heard: " + hound_transcribed) #print what was heard by houndify
			return google_transcribed
		except sr.UnknownValueError:
		    print("could not understand audio")
		except sr.RequestError as e:
		    print("Could not request results ; {0}".format(e))
	else:
		return "" #return empty string if we timed out
