#This file will hold the plug class and all methods associated with it
import requests
from dotenv import load_dotenv
import os

load_dotenv() #Used to fetch device ip (So i can hide it from github :-)
device_ip = os.getenv("DEVICE_IP")


class Plug():
    def __init__(self):
        self._running = self._get_status()
        if self._running is None:
            print("Unable to reach device, please try again")

    def _get_status(self):
        try:
            r = requests.get(f"http://{device_ip}/relay/0", timeout=3)
            data = r.json()
            return data.get("ison", None)
        except requests.exceptions.RequestException:
            return None
            
    
    def power_on(self):
        if self._running:
            print("Device is already powered on")
        else:
            try:
                r = requests.get(f"http://{device_ip}/rpc/Switch.Set?id=0&on=true", timeout=3)
                self._running = self._get_status
                print("Device was turned on")
            except requests.exceptions.RequestException:
                return None

    def power_off(self):
        if not self._running:
            print("Device is already powered off")
        else:
            try:
                r = requests.get(f"http://{device_ip}/rpc/Switch.Set?id=0&on=false", timeout=3)
                self._running = self._get_status
                print("Device was powered off")
            except requests.exceptions.RequestException:
                return None
