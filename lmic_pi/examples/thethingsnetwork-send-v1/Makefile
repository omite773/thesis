CFLAGS=-I../../lmic
PYFLAGS=-I/usr/include/python2.7 -lpython2.7 
LDFLAGS=-lwiringPi

thethingsnetwork-send-v1: thethingsnetwork-send-v1.cpp
	cd ../../lmic && $(MAKE)
	$(CC) $(CFLAGS) $(PYFLAGS) -o thethingsnetwork-send-v1 thethingsnetwork-send-v1.cpp ../../lmic/*.o $(LDFLAGS)

all: thethingsnetwork-send-v1

.PHONY: clean

clean:
	rm -f *.o thethingsnetwork-send-v1
