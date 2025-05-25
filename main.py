from plug import *
from dateandtimepicker import *
import datetime
import time

p = Plug()
datetime_picker = DateAndTimePicker()
user_selected_datetime = datetime_picker.display()


print(f"User time: {user_selected_datetime}")
print(f"Current time: {datetime.datetime.now()}")

while user_selected_datetime >= datetime.datetime.now():
    time.sleep(1)

p.power_on()
time.sleep(15)
p.power_off()