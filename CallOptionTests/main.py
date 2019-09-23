from callOptions import keyOne, keyTwo, keyThree

def main():
	# r = sr.Recognizer()
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

	# keyOne(2,1,6,4) #Run test for when the CS has pressed '1' on their phone
	keyTwo(2,1,6,4) #Run test for when the CS has pressed '2' on their phone
	# keyThree(2,1,6,4) #Run test for when the CS has pressed '3' on their phone

	return


if __name__ == '__main__':
	main()
