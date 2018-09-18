from Weather import Weather_App
import time
import sys
import argparse

parser = argparse.ArgumentParser(
    description="Weather Script to push rain notification to phone",

)
parser.add_argument("lat",type=str,help="Latitude of position to update")
parser.add_argument("long",type=str,help="Longtitude of position to update")
parser.add_argument("secret_key",type=str,help="Secretkey of DarkSky api, see readme for details")
parser.add_argument("time_to_check",type=str,help="When the script should wake up to query API")
args=parser.parse_args()

weather = Weather_App(args.lat,args.long,args.secret_key)
hour = 3600
minute = 60


# Loop that powers up at 9, checks every minute for time_to_wake
while True:
    t = weather.get_time()
    if t.hour == args.time_to_check:
        if weather.is_raining():
            weather.send_notification()
            time.sleep(hour)
    time.sleep(minute)
