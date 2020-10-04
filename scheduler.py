#!/usr/bin/env python3

import os
import schedule

# Execute a system command to display a toast notification with a custom message
def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

# Delete all empty folders in a given directory
def delete_empty_folders():
    notify('Script', 'Script is currently running')
    path = '/enter/path/here'
    os.chdir(path)  # Change working directory to the path
    directory = os.walk(path)  # Scan directory for its contents
    content = next(directory)
    for folder in content[1]:  # Loop through each folder in the path
        if not os.listdir(folder):  # If it is empty remove it
            os.rmdir(folder)

schedule.every().day.do(delete_empty_folders)
while True:
    schedule.run_pending()
