# This file instantiates a tuple of tuples which contain an audio  file paired up with its corresponding transcription
# Tuple format - (File path, Transcription)
# Sentences from: http://www.cs.columbia.edu/~hgs/audio/harvard.html
# Naming format for files: h11_s1 -> harvard list 11, sentence 1

AudioFiles = ('..\AudioFiles\h11_s1.wav','..\AudioFiles\h14_s1.wav','..\AudioFiles\h19_s2.wav','..\AudioFiles\h6_s7.wav',
			  '..\AudioFiles\h5_s3.wav','..\AudioFiles\h11_s2.wav','..\AudioFiles\h11_s4.wav','..\AudioFiles\h11_s8.wav',
			  '..\AudioFiles\h12_s2.wav','..\AudioFiles\h14_s6.wav','..\AudioFiles\h15_s6.wav',
			  '..\AudioFiles\h18_s6.wav','..\AudioFiles\h20_s8.wav','..\AudioFiles\h26_s7.wav',
			  '..\AudioFiles\h28_s2.wav','..\AudioFiles\h30_s4.wav','..\AudioFiles\h32_s7.wav','..\AudioFiles\h34_s5.wav',
			  '..\AudioFiles\h35_s10.wav','..\AudioFiles\h38_s9.wav','..\AudioFiles\h39_s3.wav','..\AudioFiles\h45_s4.wav')


Transcriptions = (	"oak is strong and also gives shade",
					"a cramp is no small danger on a swim",
					"fairy tales should be fun to write",
					"march the soldiers past the next hill",
					"sickness kept him home the third week",
					"cats and dogs each hate the other",
					"open the crate but don't break the glass",
					"act on these orders with great speed",
					"leaves turn brown and yellow in the fall",
					"bring your problems to the wise chief",
					"purebred poodles have curls",
					"sunday is the best part of the week",
					"bring your best compass to the third class",
					"ducks fly north but lack a compass",
					"find the twin who stole the pearl necklace",
					"watch the log float in the wide river",
					"screw the round cap on as tight as needed",
					"pages bound in cloth make a book",
					"next tuesday we must vote",
					"soap can wash most dirt away",
					"grape juice and water mix well",
					"breakfast buns are fine with a hot drink"
					)


# Zip the two tuples together into a tuple of tuples called hs
hs=tuple(zip(AudioFiles,Transcriptions))
