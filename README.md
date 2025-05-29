# ☕ CoffeAutomation – Schedule with GUI or CLI

This python project automates powering on a coffemaker with the help of a smartplug (Shell Plug 3s in my case).
It supports scheduling with both CLI and GUI

## Functionality

- Power on and off coffemaker through wifi
- Chose brew time through GUI (Calendar and clock) or CLI
- Is very easily adapted to any other device that allows for local api control

##  Projecstructure

📁 your-project/
├── main.py
├── plug.py
├── dateandtimepicker.py
├── terminal_input.py
├── .env
├── requirements.txt
└── README.md

##  Installation

1. Clone project or download the code
2. Create a virtual environment (Not required, but recommended).
    python -m venv venv
    MacOS: source venv/bin/activate
    Windows: venv\Scripts\activate
3. Install dependencies
    pip install -r requirements.txt
4. Create a file called .env in your project folder and add:
    DEVICE_IP=192.168.X.X
    Replace ip with the ip for your smart plug

##  Running the program

1. Run the program with Python main.py (May be python3 main.py depending on your python version)
2. Chose GUI or Terminal
3. Add the times you want to schedule
4. Coffemaker will turn on on the scheduled time and turned off after 10 minutes (This may have to be altered depending on your coffeemaker. there is a comment in the code for this)


##  Possible improvements
1. Add push notis for when coffee is brewed
2. Improvments for calendar, allow user to remove scheuled times
3. WebUI accessible from outside the local dev environment