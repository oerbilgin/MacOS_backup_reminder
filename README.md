# MacOS_backup_reminder
## A small python script that looks to see when the last time a Time Machine backup was made, and if it was too long ago, pings a reminder
* I have only tested this on MacOS Sierra 10.12.3

![example alert](https://github.com/oerbilgin/MacOS_backup_reminder/blob/master/example_alert.png)

## Installation
1. Install Python 2.7
2. Copy the .py file into a directory of your choice
2. Determine your age of backup trigger, in number of days
  1. Call the script with the flag `-d` or `--days` followed by the number of days you want before the backup alert triggers
  2. For example, if you put 3, once the last backup is 3 or more days old, you will get pinged
3. Create a cron job:
  1. `crontab -e` to edit your crontab, which opens it in vi
  2. insert a cron job that runs the script as often as you want. For example, this job which will run every 10 minutes and remind you once your last backup is 3 or more days old
  ```bash
  */10 * * * * python <path_to_script>/backup_monitor.py -d 3
  ```
