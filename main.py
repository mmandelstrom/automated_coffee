from plug import *
from dateandtimepicker import *
from datetime import datetime
import time

p = Plug() 

print("Would you like to use GUI or terminal to scheudle your coffee?")

while True:
    print("Type GUI or Terminal: ")
    user_input = input()

    if user_input.lower() == "gui":
        datetime_picker = DateAndTimePicker()
        user_selected_datetime = datetime_picker.display()

        try:
            datetime_picker.root.update() #Workaround to solve calendar not closing after clicking submit. Eventloop got blocked by while loop
        except tk.TclError:
            pass
        break

    elif user_input.lower() == "terminal":
        print("Please enter date and time in this format: YYYY-MM-DD HH:MM")
        user_datetime = input()
        user_selected_datetime = datetime.strptime(f"{user_datetime}", "%Y-%m-%d %H:%M")
        break

    else:
        print("Invalid input")
        continue

    

print(f"User time: {user_selected_datetime}")
print(f"Current time: {datetime.now()}")

while user_selected_datetime >= datetime.now():
    time.sleep(1)

""" Need to implement full schedule using dict with brewed/not brewed values
"""

p.power_on()
time.sleep(15)
p.power_off()