import subprocess

player = "paplay"
soundLibraryPath = "sound-library/"
audioFileType = ".ogg"


tmnFile = open("songs/first.tmn", "r")
notes = tmnFile.read().replace('\n', '').split('/')
print(notes)

for note in notes:
	subprocess.run([player, soundLibraryPath + note + audioFileType])