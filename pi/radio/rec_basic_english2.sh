#!/bin/sh

#cd /mnt/hdd1/shared/radio
cd /home/pi/shared/radio

if test -n "`ls -t . | tail -n+12`";then
	rm -v `ls -t . | tail -n+12`
fi
