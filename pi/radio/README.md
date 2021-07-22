# crontab -e

run `crontab -e`, so add cron schedules.

- 06:30 on weekday: record basic english 3
- 21:30 on weekday: record basic english 3
- 00:00 on everyday: delete old files
- 09:10 on weekday: record enjoy simple english
- 16:25 on weekday: record enjoy simple english

```sh

30 06 * * 1-5 /home/pi/cron/rec_basic_english3.sh
30 21 * * 1-5 /home/pi/cron/rec_basic_english3.sh backup
00 00 * * * /home/pi/cron/del_old.sh
10 09 * * 1-5 /home/pi/cron/rec_enjoy_simple_english.sh
25 16 * * 1-5 /home/pi/cron/rec_enjoy_simple_english.sh backup

```
