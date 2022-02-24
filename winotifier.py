from win10toast import ToastNotifier
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import requests
import json

def notification():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    toaster = ToastNotifier()
    toaster.show_toast("😰 DEHYDRATION ALERT!","Hi Utpal it's ⏰"+current_time+" already, Grab yourself a glass of cool water 🥤",duration=10)
    print("Drink Water Reminder Sent!")

def random_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    # Use GET request
    response = requests.request("GET", url)
    # Load the request in json file
    data = json.loads(response.text)
    # we will need 'text' from the list, so 
    # pass 'text' in the list
    useless_fact = data['text']
    toaster = ToastNotifier()
    toaster.show_toast("🤔 DID YOU KNOW?",'😱 '+useless_fact,duration=5)
    print("Random fact Sent!")

scheduler = BlockingScheduler()
scheduler.add_job(random_fact, 'interval', seconds=10)
scheduler.start()
