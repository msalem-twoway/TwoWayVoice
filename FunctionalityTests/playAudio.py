import pyaudio
import wave
import time
import sys

# This function uses the pyaudio library play an audio file
# Expected behavior: A speaker will be selected based on the index and will attempt
# toplay the audio file given
# INPUTS:	index - the deivce index to set the speaker to play from
#			file - which audio file to play
# OUTPUTS:	none
def playAudio(index,file):
	wf = wave.open(file, 'rb')

	# instantiate PyAudio (1)
	p = pyaudio.PyAudio()

	# define callback (2)
	def callback(in_data, frame_count, time_info, status):
	    data = wf.readframes(frame_count)
	    return (data, pyaudio.paContinue)

	# open stream using callback (3)
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
	                channels=wf.getnchannels(),
	                rate=wf.getframerate(),
	                output=True,
	                output_device_index=index,
	                stream_callback=callback)

	#Start and stop the audio so that we can wait for the mic to adjust for background noise
	stream.start_stream()
	stream.stop_stream()
	time.sleep(4)
	stream.start_stream()

	# wait for stream to finish (5)
	while stream.is_active():
		time.sleep(0.1)

	# stop stream (6)
	stream.stop_stream()
	# print("audio finished")
	stream.close()
	wf.close()

	# close PyAudio (7)
	p.terminate()
