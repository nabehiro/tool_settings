#!/bin/sh

if [ "$1" = "backup" ]
then
	path=/home/pi/shared/radio/backup/`date "+%m%d(%a)"`_enjoy-simple-english.m4a
else
	path=/home/pi/shared/radio/`date "+%m%d(%a)"`_enjoy-simple-english.m4a
fi

url=http://nhkradioakr2-i.akamaihd.net/hls/live/511929/1-r2/1-r2-01.m3u8

ffmpeg -i $url -t 360 -c copy $path
