import speech_recognition as sr
import sys

r = sr.Recognizer()
r.pause_threshold=0.5 #Stop listening after 0.5 seconds of no activity
timeout=False
mic = sr.Microphone(device_index=int(sys.argv[1])) #set microphonse to the correct index

with mic as source:
    #print("adjusting levels...")
    audio = r.adjust_for_ambient_noise(source,duration=2) #adjust for background noise for 2 seconds
    #print("Speak into the mic:")
    try:
	audio = r.listen(source,timeout=5) #start listening on the mic, timeout if nothing is heard after 5 seconds
    except sr.WaitTimeoutError: #catch the timeout exception and record that we timed out
	timeout=True;
if not timeout:
	try:
	    # print("Processing...")
	    #google_transcribed = r.recognize_google(audio) #call google speech services to process what was heard on the mic
	    recog = r.recognize_wit(audio, key = "6Y4KLO4YTWDQSYQXGONPHAVB3IRSWFRN")
	    print(recog) #print what was heard by google
	except sr.UnknownValueError:
	    print("could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results ; {0}".format(e))
else:
	print("Timed out") #return empty string if we timed out
