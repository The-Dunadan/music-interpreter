import subprocess
import time
import os


# constants
player = "paplay"
soundLibraryPath = "sound-library/"
songLibraryPath = "songs/"
audioFileType = ".ogg"
instruments = ["electrical-guitar/", "violin/"]


# user input
songs = os.listdir(songLibraryPath)
songs.sort()
for i in range(len(songs)):
	print(str(i + 1) + ". " + songs[i])
songNumber = int(input('Type in the number coresponding to the song '
					 + 'you would like to hear or 0 if you would like '
					 + 'to provide your own song: ')) - 1
for i in range(len(instruments)):
	print(str(i + 1) + ". " + instruments[i])
instrument = int(input('Type the number coresponding to the instrument '
					 + 'you would like to hear interpreting the song: ')) - 1

if songNumber >= 0:
	tmnFile = open(songLibraryPath + songs[songNumber], "r")
	chords = tmnFile.read().replace('\n', '').split('/')
	tmnFile.close()
	print(chords)
else:
	#TODO
	exit()


# compute chord durations
durations = [0] * len(chords)
for i in range(len(chords)):
	chord = chords[i]
	for j in range(len(chord)):
		if chord[j] == '-':
			duration = chord[j + 1:]
			duration = duration[0 : (duration.find('|') if duration.find('|') != -1 
				                                        else len(duration))]
			if int(duration) > durations[i]:
				durations[i] = int(duration)


# play the song
for i in range(len(chords)):
	chord = chords[i]
	print(chord)
	notes = chord.split('|')
	for note in notes:
		subprocess.Popen([player, soundLibraryPath + instruments[instrument] 
			                                       + note + audioFileType])
	time.sleep(4/durations[i])