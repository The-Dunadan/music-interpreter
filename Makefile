CC=gcc
CFLAGS=-Wall

build:
	$(CC) $(CFLAGS) main.c -o main.out

clean:
	rm *.out