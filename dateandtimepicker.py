#This file will hold calendar and related functions
from datetime import datetime
from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar
from tktimepicker import SpinTimePickerModern, constants

class DateAndTimePicker():
    def __init__(self, terminal=False):
        self.selected_datetime = {}
        self.root = tk.Tk()
            

    def gui(self):
        #Date selector
        current_date = datetime.today()
        style = ttk.Style(self.root)
        style.theme_use('clam')
        year, month, day = current_date.year, current_date.month, current_date.day #Get year, month, day to limit calendar to todays date and on
        tk.Label(self.root, text="Select date:").pack()
        calendar = Calendar(self.root, date_pattern='yyyy-mm-dd', mindate=datetime(year, month, day),
                            showweeknumbers = False, showothermonthdays = False,
                            normalforeground = "black", selectforeground = "coral",
                            headersforeground = "black", background = "bisque",
                            foreground = "black", selectbackground = "bisque") #Create a calendar
        
        calendar.pack(pady=5)
        
        #Time selector
        tk.Label(self.root, text="Select time:").pack(ipadx=100)
        time_picker = SpinTimePickerModern(self.root) #Create clock
        time_picker.addAll(constants.HOURS24)
        time_picker.pack(pady=5)


        def submit():
            self.root.after(0, self.root.destroy)

        def add_to_schedule():
            date = calendar.get_date() #Get date
            hour = time_picker.hours() #Get hour
            minute = time_picker.minutes() #Get minute
            date_time = datetime.strptime(f"{date} {hour}:{minute}", "%Y-%m-%d %H:%M")
            if date_time < datetime.now():
                print("Time chosen is in the past, please chose a new time")
            else:
                self.selected_datetime[date_time] = False
                print(f"Added {date_time} to the schedule, add more times or use submit to close calendar")
            

        tk.Button(self.root, text="Add to schedule", command=add_to_schedule).pack()
        tk.Button(self.root, text="Submit", command=submit).pack(pady=15)
        
        self.root.mainloop()
        return self.selected_datetime