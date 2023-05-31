# Usage

1. Install libraries
`python -m pip install -r requirements.txt`

2. Edit `main.py` script to add your custom logic 
(change `LIMIT` variable and add logic to price comparison `if`s)

[Raspberry Pi GPIO](https://pimylifeup.com/raspberry-pi-gpio/)

3. Add a cronjob to run this script once per hour (or modify the script to 
store the data for the day and only run it once per day)

[How to set up a cron job](https://phoenixnap.com/kb/set-up-cron-job-linux)

NOTE: Tested with python 3.8 (should work with any python between 3.7 and 3.9)
