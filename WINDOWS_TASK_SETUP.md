# Windows Task Scheduler Setup

## Method 1: Import XML
1. Open Task Scheduler (taskschd.msc)
2. Click "Import Task..." in the right panel
3. Select UmaRaceUpdate.xml
4. Click OK

## Method 2: Manual Setup
1. Open Task Scheduler
2. Create Basic Task...
3. Name: "UmamusumeAutoTrainer Race Update"
4. Trigger: Weekly, Monday, 3:00 AM
5. Action: Start a program
6. Program: F:\ULTIMA\UmamusumeAutoTrainer\scheduled_update.bat
7. Finish

## Test the task:
1. Right-click the task → Run
2. Check logs in: logs\race_update_*.log
