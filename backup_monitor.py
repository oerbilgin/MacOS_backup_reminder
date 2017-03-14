'''
Short script to detect when the last backup was, and alerts when you haven't backed up in over a week
'''

import subprocess
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--days', help='How many days ago your last backup was to trigger the alert', required=True, type=int)
args = parser.parse_args()

cmd = '/usr/libexec/PlistBuddy -c "Print Destinations:0:SnapshotDates" /Library/Preferences/com.apple.TimeMachine.plist '
backups = subprocess.check_output(cmd, shell=True)

# get the last backup
last_backup = backups.split('{')[1].split('}')[0].split('\n')[-2].split('    ')[1]

last_backup = datetime.datetime.strptime(last_backup, '%a %b %d %H:%M:%S %Z %Y')

#calculate the time since last backup and alert if it's been 7 or more days
today = datetime.datetime.today()
delta = (today - last_backup)
if delta.days >= args.days:
    cmd = 'osascript -e \'display notification "Last backup is %s days old!" with title "Backup NOW!" sound name "Basso"\'' %(delta.days)
    subprocess.Popen(cmd, shell=True)
