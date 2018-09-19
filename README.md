# Weather_App
Python Script for generating Weather Push Notifs -- current iteration supports only rain 
Powered by DarkSky API

## Pre-requisites 
* Run the following: 
* pip install notify-run
* notify-run register 
* Follow the intstructions to link phone to notification serivce 

## Positional arguments
* lat -- Latitude of the GPS coordinates to query 
* long -- Longitude of the GPS coordinates to query 
* secret_key -- DarkSky API Secret key, register here: https://darksky.net/dev/register
* time_to_check -- Time the script will check for rain (idea is when you wake up, send push notif if raining) 
