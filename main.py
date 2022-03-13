# Importing the csv2json module.
import csv2json

header: str = '''
  /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$
 |______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/

   /$$$$$$   /$$$$$$  /$$    /$$ /$$$$$$$$ /$$$$$$          /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$
  /$$__  $$ /$$__  $$| $$   | $$|__  $$__//$$__  $$        |__  $$ /$$__  $$ /$$__  $$| $$$ | $$
 | $$  \__/| $$  \__/| $$   | $$   | $$  | $$  \ $$           | $$| $$  \__/| $$  \ $$| $$$$| $$
 | $$      |  $$$$$$ |  $$ / $$/   | $$  | $$  | $$           | $$|  $$$$$$ | $$  | $$| $$ $$ $$
 | $$       \____  $$ \  $$ $$/    | $$  | $$  | $$      /$$  | $$ \____  $$| $$  | $$| $$  $$$$
 | $$    $$ /$$  \ $$  \  $$$/     | $$  | $$  | $$     | $$  | $$ /$$  \ $$| $$  | $$| $$\  $$$
 |  $$$$$$/|  $$$$$$/   \  $/      | $$  |  $$$$$$/     |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$ \  $$
  \______/  \______/     \_//$$$$$$|__/   \______//$$$$$$\______/  \______/  \______/ |__/  \__/
                           |______/              |______/

 Coded by: Angel Badillo Hernandez

  /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$
 |______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/
 '''

promptCSV: str = "  Enter the name of the csv file >> "
doneMsg: str = "\n  Conversion is complete!!!"
footer: str = '''
  /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$
 |______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/
'''

# Printing the header of the program.
print(header)

# Asking the user to enter the name of the csv file.
csvName: str = input(promptCSV)

# This is a way to change the file extension for the name of the file.
jsonName: str = csvName.replace("csv", "json")

# This is a function that converts a csv file to a json file.
csv2json.csv_to_json(csvName, jsonName)

# Printing a message to the user that the conversion is done.
print(doneMsg)

# Printing the footer of the program.
print(footer)
