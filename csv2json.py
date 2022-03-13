#   /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$
#  |______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/
                                                                                                                                                                                        
#    /$$$$$$   /$$$$$$  /$$    /$$ /$$$$$$$$ /$$$$$$          /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$ 
#   /$$__  $$ /$$__  $$| $$   | $$|__  $$__//$$__  $$        |__  $$ /$$__  $$ /$$__  $$| $$$ | $$ 
#  | $$  \__/| $$  \__/| $$   | $$   | $$  | $$  \ $$           | $$| $$  \__/| $$  \ $$| $$$$| $$ 
#  | $$      |  $$$$$$ |  $$ / $$/   | $$  | $$  | $$           | $$|  $$$$$$ | $$  | $$| $$ $$ $$ 
#  | $$       \____  $$ \  $$ $$/    | $$  | $$  | $$      /$$  | $$ \____  $$| $$  | $$| $$  $$$$ 
#  | $$    $$ /$$  \ $$  \  $$$/     | $$  | $$  | $$     | $$  | $$ /$$  \ $$| $$  | $$| $$\  $$$ 
#  |  $$$$$$/|  $$$$$$/   \  $/      | $$  |  $$$$$$/     |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$ \  $$ 
#   \______/  \______/     \_//$$$$$$|__/   \______//$$$$$$\______/  \______/  \______/ |__/  \__/ 
#                            |______/              |______/                                        
                                                                                                                                                                                                  
#  Coded by: Angel Badillo Hernandez                                                                                             
                                                                                                                                                                                                
#   /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$
#  |______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/
import csv
import json

def csv_to_list(fileName: str) -> list:
    """
    Reads a csv file and returns a list of dictionaries
    
    :param fileName: str = the name of the file to be read
    :type fileName: str
    :return: A list of dictionaries.
    """
    ls: list = list()
    with open(fileName, 'r') as csvFile:
        reader = csv.DictReader(csvFile) 
    
        for obj in reader:
            ls.append(obj)
    return ls

def list_to_json(ls: list, fileName: str) -> None:
    """
    Convert a list to a json file
    
    :param ls: the list you want to convert to JSON
    :type ls: list
    :param fileName: the name of the file you want to save the json to
    :type fileName: str
    """
    with open(fileName, 'w') as jsonFile:
        json.dump(ls, jsonFile)

def csv_to_json(csvName: str, jsonName: str) -> None:
    """
    Convert a csv file to a json file
    
    :param csvName: The name of the CSV file to be converted to JSON
    :type csvName: str
    :param jsonName: the name of the json file you want to create
    :type jsonName: str
    """
    list_to_json(csv_to_list(csvName), jsonName)