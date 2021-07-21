#!/bin/sh

cd /home/pi/shared/radio

if test -n "`ls -t . | tail -n+12`";then
	rm -v `ls -t . | tail -n+12`
fi


cd /home/pi/shared/radio2

if test -n "`ls -t . | tail -n+12`";then
	rm -v `ls -t . | tail -n+12`
fi
