#This file will hold calendar and related functions
from datetime import datetime
import tkinter as tk
from tkcalendar import Calendar
from tktimepicker import SpinTimePickerModern, constants

class DateAndTimePicker():
    def __init__(self):
        self.selected_datetime = None #Value that will be returned and used to activate plug
        self.root = tk.Tk()


    def display(self):
        #Date selector
        current_date = datetime.today()
        year, month, day = current_date.year, current_date.month, current_date.day #Get year, month, day to limit calendar to todays date and on
        tk.Label(self.root, text="Select date:").pack()
        calendar = Calendar(self.root, date_pattern='yyyy-mm-dd', mindate=datetime(year, month, day),
                            showweeknumbers = False, showothermonthdays = False) #Create a calendar
        calendar.pack(pady=10)
        
        #Time selector
        tk.Label(self.root, text="Select time:").pack(pady=10)
        time_picker = SpinTimePickerModern(self.root) #Create clock
        time_picker.addAll(constants.HOURS24)
        time_picker.pack(pady=10)

        def submit():
            date = calendar.get_date() #Get date
            hour = time_picker.hours() #Get hour
            minute = time_picker.minutes() #Get minute
            self.selected_datetime = datetime.strptime(f"{date} {hour}:{minute}", "%Y-%m-%d %H:%M") #Combine and save

            self.root.destroy()

        tk.Button(self.root, text="Submit", command=submit).pack()
        self.root.mainloop()

        return self.selected_datetime


picker = DateAndTimePicker()
valt_datum_tid = picker.display()
print(valt_datum_tid)
