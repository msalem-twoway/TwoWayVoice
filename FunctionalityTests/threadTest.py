import threading
import time

from speakerTest import speakerTest

panel_audio_thread=threading.Thread(target=speakerTest, args=(6,'..\AudioFiles\harvard1_5sec.wav'))
panel_audio_thread.setDaemon(True)
panel_audio_thread.start()
while panel_audio_thread.isAlive():
	time.sleep(0.1)