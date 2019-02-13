import subprocess
import re
import time

player = "paplay"
soundLibraryPath = "sound-library/"
audioFileType = ".ogg"


tmnFile = open("songs/hobbit's song.tmn", "r")
chords = tmnFile.read().replace('\n', '').split('/')
print(chords)

durations = [0] * len(chords)
for i in range(len(chords)):
	chord = chords[i]
	print(chord)
	for j in range(len(chord)):
		if chord[j] == '-':
			duration = chord[j + 1:]
			duration = duration[0 : (duration.find('|') if duration.find('|') != -1 
				                                        else len(duration))]
			#print(int(duration))
			if int(duration) > durations[i]:
				durations[i] = int(duration)

#print(durations)

for i in range(len(chords)):
	chord = chords[i]
	print(chord)
	notes = chord.split('|')
	for note in notes:
		subprocess.Popen([player, soundLibraryPath + note + audioFileType])
	time.sleep(4/durations[i])