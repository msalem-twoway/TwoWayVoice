import pyaudio
import wave
import time
import sys


def speakerTest(index,file):
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
	# print("in playaudio")
	time.sleep(1)
	# print("1 sec sleep")
	stream.start_stream()
	# print("playing audio")
	# # wait for stream to finish (5)
	while stream.is_active():
		time.sleep(0.1)

	# stop stream (6)
	stream.stop_stream()
	# print("audio finished")
	stream.close()
	wf.close()

	# close PyAudio (7)
	p.terminate()
