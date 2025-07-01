# UmamusumeAutoTrainer Race Update Cron Setup

## Daily Update (Every day at 3 AM)
0 3 * * * cd /mnt/f/ULTIMA/UmamusumeAutoTrainer && /usr/bin/python3 scheduled_update.py

## Weekly Update (Every Monday at 3 AM)  
0 3 * * 1 cd /mnt/f/ULTIMA/UmamusumeAutoTrainer && /usr/bin/python3 scheduled_update.py

## How to setup:
1. Run: crontab -e
2. Add one of the above lines
3. Save and exit

## Check logs:
tail -f logs/race_update_*.log
