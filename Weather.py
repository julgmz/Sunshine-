import requests
import json
import sys
import datetime
from notify_run import Notify


class Weather_App:
    def __init__(self,latitude,longitude,secret_key):
        self.encoding = "utf-8"
        self.latitude = latitude
        self.longitude = longitude
        self.location = self.latitude + "," + self.longitude
        self.dark_sky_endpoint = "https://api.darksky.net/forecast/" + secret_key + "/"
        self.data = self.query()

    def query(self):
        request = self.dark_sky_endpoint + self.location
        print("Powered by Dark Sky\n"
              "https://darksky.net/poweredby/" )
        response = requests.get(request) # can error here
        content = json.loads(response.content.decode(self.encoding))
        return content["daily"]["data"][0]


    def is_raining(self):
        if self.data["icon"] == "rain":
            return True
        return False

    def send_notification(self):
        notify = Notify()
        notify.send("RAIN ALERT\n" +
                    self.data["summary"])

    def get_time(self):
        now = datetime.datetime.now()
        return now




