from plug import *
from dateandtimepicker import *
from datetime import datetime
import time
from terminal_input import *

p = Plug()

print("Would you like to use GUI or terminal to scheudle your coffee?")

while True:
    print("Type GUI or Terminal: ")
    user_input = input()

    if user_input.lower() == "gui":
        datetime_picker = DateAndTimePicker()
        user_selected_datetime = datetime_picker.gui()
        try:
            datetime_picker.root.update() #Workaround to solve calendar not closing after clicking submit. Eventloop got blocked by while loop
        except tk.TclError:
            pass
        break

    elif user_input.lower() == "terminal":
        user_selected_datetime = terminal_user_input()
        break

    else:
        print("Invalid input")
        continue

    
for key, value in user_selected_datetime.items():
    print(f"User time: {key}")
print(f"Current time: {datetime.now()}")

while True:
    for key, value in user_selected_datetime.items():
        if key <= datetime.now() and value == False:
            user_selected_datetime[key] = True
            p.power_on()
            time.sleep(600)
            p.power_off()
    time.sleep(1)
    if False not in user_selected_datetime.values():
        break