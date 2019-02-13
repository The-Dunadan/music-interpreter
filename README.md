# music-interpreter

The initial purpose of this project is to create a file format and a program
that can interpret it in order to call on the operating system and play the
sounds we desire (from a sound library that we provide).
Idealy, this would be extended with an algorithm that reads sheet music from
pictures and translates in to the file format which can be played.

Planned assets:
- Sheet music reader and translator
- File format equivalent to sheet music
- Text to sound interpretor
- Sound library


Musical notation:\
A note is represented as follows: "[a-g][s,n,f][1-8]-[1-9]+([\.]?[0-9]+)?" and delimited with '|' (pipe symbol).\
Explanation:
- First character represents the note, 'a' to 'g'.
- Second character represents the pitch alteration ('s' for sharp, 'f' for flat, 'n' for natural).
- Third character represents the octave in one digit.
- Fourth character is a delimitor, '-'
- Then comes the duration of the note. E.g: 4 for a quarter note, 8 for an eight, etc.

Notes played simultaneously (call them chords) are delimited by '/' (forward slash). The next chord is played after the shortest of the notes is finished playing.