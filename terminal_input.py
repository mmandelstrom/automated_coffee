#This file will hold functions relating to userinput from terminal
from datetime import datetime

def terminal_user_input():
    selected_datetime = {}
    while True:
        print("Please enter date and time in this format: YYYY-MM-DD HH:MM")
        user_datetime = input()
        date_time = datetime.strptime(f"{user_datetime}", "%Y-%m-%d %H:%M")
        if date_time < datetime.now():
            print("Time chosen is in the past, please input a new date and time")
        else:
            selected_datetime[date_time] = False
        print(f"Added {date_time} to the schedule")
        print("Click Y to input another time or any other key to submit: ")
        user_cont = input()
        if user_cont.lower() == "y":
            continue
        else:
            return selected_datetime