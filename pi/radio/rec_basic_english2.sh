#!/bin/sh

if [ "$1" = "backup" ]
then
	#path=/mnt/hdd1/shared/radio/backup/`date "+%m%d(%a)"`_基礎英語２.m4a
	path=/home/pi/shared/radio/backup/`date "+%m%d(%a)"`_基礎英語２.m4a
else
	#path=/mnt/hdd1/shared/radio/`date "+%m%d(%a)"`_基礎英語２.m4a
	path=/home/pi/shared/radio/`date "+%m%d(%a)"`_基礎英語２.m4a
fi

url=http://nhkradioakr2-i.akamaihd.net/hls/live/511929/1-r2/1-r2-01.m3u8

ffmpeg -i $url -t 960 -c copy $path
