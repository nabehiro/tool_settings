#!/bin/sh

# delete old files of "Basic English 3"
cd /home/pi/shared/radio

if test -n "`ls -t . | tail -n+12`";then
	rm -v `ls -t . | tail -n+12`
fi

# delete old files of "Enjoy Simple English"
cd /home/pi/shared/radio2

if test -n "`ls -t . | tail -n+12`";then
	rm -v `ls -t . | tail -n+12`
fi
