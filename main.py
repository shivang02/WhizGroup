"""
WhatsApp Group Maker

Description:
This program automates the process of creating WhatsApp groups by adding contacts from a CSV file to a new group. It utilizes the Selenium library to control the Chrome web browser and perform the necessary operations on WhatsApp Web.

Motivation:
Creating WhatsApp groups manually can be a tedious and time-consuming task, particularly when dealing with a large number of contacts. The purpose of this project is to streamline the group creation process and enhance efficiency by automating the necessary steps.

Features:

* Enables selection of a CSV file containing contact details for the group members.
* Downloads the Chrome driver automatically.
* Opens WhatsApp Web in a Chrome browser.
* Displays a countdown timer for the user to log in to WhatsApp Web.
* Adds the contacts from the CSV file to a new group on WhatsApp.
* Provides a user-friendly graphical interface for easy interaction.

Instructions:

1. Click the 'Browse' button to select the CSV file containing the contact details.
2. Once the file is selected, click the 'Start' button to initiate the group creation process.
3. Log in to WhatsApp Web within 40 seconds.
5. The program will automatically add the contacts to a new group on WhatsApp.
6. The group name can be entered manually after the group is created.
7. Close the program once the group is created.

Note: Ensure that you have a stable internet connection and the necessary permissions to access WhatsApp Web.

"""

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
from ttkthemes import ThemedTk
import subprocess

# Function to download the Chrome driver
def download_driver():
    ChromeDriverManager().install()

# Function to handle the file selection button click
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(tk.END, file_path)

# Function to get the file path
def get_file_path():
    file_path = file_entry.get()
    return file_path

# Function to open WhatsApp Web
def open_whatsapp_web(contacts_file):
        # Download the Chrome driver
        download_driver()

        # Create the Chrome driver
        options = webdriver.ChromeOptions()
        global driver
        driver = webdriver.Chrome(service=ChromeService(), options=options)

        # Open WhatsApp Web    
        driver.get("https://web.whatsapp.com")

        # Start the countdown
        update_countdown()

        # Wait for 40 seconds before performing the operations
        window.after(5000, perform_whatsapp_operations, driver, contacts_file)

countdown_update_id = None

# Function to handle the start button click
def start_program():
    # If the contacts file is selected, open WhatsApp Web
    contacts_file = get_file_path()
    try:
        if contacts_file:
            open_whatsapp_web(contacts_file)
        else:
            raise Exception("File not selected")
    except Exception as e:
        print(e)
        # Create a pop-up window to inform the user that the file was not selected
        file_error_window = tk.Toplevel(window)
        file_error_window.title("File Error")
        file_error_label = ttk.Label(file_error_window, text="Please select a file")
        file_error_label.pack(padx=10, pady=10)
        file_error_button = ttk.Button(file_error_window, text="OK", command=file_error_window.destroy)
        file_error_button.pack(padx=10, pady=10)
        
        # position it on the top of all windows
        file_error_window.attributes('-topmost', True)
        file_error_window.after_idle(file_error_window.attributes, '-topmost', False)
        
        # set the window in the center of the screen
        file_error_window_width = 200
        file_error_window_height = 100
        screen_width = file_error_window.winfo_screenwidth()
        screen_height = file_error_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (file_error_window_width / 2))
        y_coordinate = int((screen_height / 2) - (file_error_window_height / 2))
        file_error_window.geometry("{}x{}+{}+{}".format(file_error_window_width, file_error_window_height, x_coordinate, y_coordinate))

        # Restart the window
        window.mainloop()

# Function to perform the WhatsApp operations
def perform_whatsapp_operations(driver, contacts_file):

    # Read contacts from the CSV file
    df = pd.read_csv(contacts_file)
    contacts = df['Name'].tolist()

    # Try to perform the operations
    try:
        
        # Clicking on the three dots to open the menu
        menu_locator = '/html/body/div[1]/div/div/div[4]/header/div[2]/div/span/div[4]/div/span'
        menu = driver.find_element("xpath", menu_locator)
        menu.click()

        # Clicking on the new group button
        new_group_locator = '/html/body/div[1]/div/div/div[4]/header/div[2]/div/span/div[4]/span/div/ul/li[1]'
        new_group = driver.find_element("xpath", new_group_locator)
        new_group.click()

        # Searching for the contacts and adding them to the group
        for contact in contacts:
            time.sleep(1)
            search_locator = '//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div/div[1]/div/div/div[2]/input'
            search = driver.find_element("xpath", search_locator)
            search.send_keys(contact)
            search.send_keys(Keys.ENTER)
            search.clear()

        # Clicking on the next button
        next_button_locator = '/html/body/div[1]/div/div/div[3]/div[1]/span/div/span/div/div/span/div'
        next_button = driver.find_element("xpath", next_button_locator)
        next_button.click()

    except:

        # Create a pop-up window to inform the user that the login was not successful
        login_error_window = tk.Toplevel(window)
        login_error_window.title("Login Error")

        # set the window in the center of the screen
        login_error_window_width = 200
        login_error_window_height = 100
        screen_width = login_error_window.winfo_screenwidth()
        screen_height = login_error_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (login_error_window_width / 2))
        y_coordinate = int((screen_height / 2) - (login_error_window_height / 2))
        login_error_window.geometry("{}x{}+{}+{}".format(login_error_window_width, login_error_window_height, x_coordinate, y_coordinate))
        login_error_label = ttk.Label(login_error_window, text="Login was not successful")
        login_error_label.pack(padx=10, pady=10)
        login_error_button = ttk.Button(login_error_window, text="OK", command=login_error_window.destroy)
        login_error_button.pack(padx=10, pady=10)


        # close the driver
        driver.quit()
        
        # stop the countdown and restart the window
        stop_countdown()
        reset_countdown()
        window.mainloop()
    time.sleep(200) # Waiting for the group to be created, group name to be entered, and group to be opened

# Create the GUI window
window = ThemedTk(theme="radiance")
window.title("WhatsApp Group Maker")
window_width = 580
window_height = 200

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

window.attributes('-topmost', True)
window.after_idle(window.attributes, '-topmost', False)

# File selection button
file_label = ttk.Label(window, text="Select Contacts File:")
file_label.grid(row=0, column=0, padx=10, pady=10)
file_entry = ttk.Entry(window, width=40)
file_entry.grid(row=0, column=1, padx=10, pady=10)
file_button = ttk.Button(window, text="Browse", command=select_file)
file_button.grid(row=0, column=2, padx=10, pady=10)

# Start button
start_button = ttk.Button(window, text="Start", command=start_program)
start_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Add a label that indicates the countdown is for the user to login to WhatsApp Web
login_label = ttk.Label(window, text="Login to WhatsApp Web within 40 seconds")
login_label.grid(row=1, column=0, columnspan=3, pady=10)

# Countdown label
countdown_label = ttk.Label(window, text="Time Left: 40 seconds")
countdown_label.grid(row=2, column=0, columnspan=3, pady=10)

# Countdown variable
countdown = 40
countdown_active = True

# Function to update the countdown label
def update_countdown():
    # Use the global variable
    global countdown, countdown_active, countdown_update_id
    countdown -= 1
    countdown_label.configure(text=f"Time Left: {countdown} seconds")
    if countdown > 0 and countdown_active:
        # Schedule the next countdown update
        countdown_update_id = window.after(1000, update_countdown)
    else:
        # Stop the countdown updates
        countdown_active = False

# Function to stop the countdown updates
def stop_countdown():
    print("Stopping countdown")
    global countdown_active, countdown_update_id
    countdown_active = False
    window.after_cancel(countdown_update_id)

# Function to reset the countdown
def reset_countdown():
    print("Resetting countdown")
    global countdown, countdown_active
    countdown = 40
    countdown_active = True
    countdown_label.configure(text=f"Time Left: {countdown} seconds")

# 
def on_closing():
    global driver
    window.destroy()  # Close the Tkinter window
    try:
        driver.quit()  # Close the WebDriver if it is still running
    except NameError:
        pass
    print("Exiting program")
    exit()  # Exit the program
    

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()

# reset the counter