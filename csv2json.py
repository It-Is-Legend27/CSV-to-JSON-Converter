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
    '''
    @brief Converts a csv file into a list of dict
    @param fileName: str - Name of the csv file
    @return list of dict
    '''
    ls: list = list()
    with open(fileName, 'r') as csvFile:
        reader = csv.DictReader(csvFile) 
    
        for obj in reader:
            ls.append(obj)
    return ls

def list_to_json(ls: list, fileName: str) -> None:
    '''
    @brief Converts a list of dict into a json file
    @param ls: list - list to convert to json file
    @param fileName: str - name of the json File
    @return None
    '''
    with open(fileName, 'w') as jsonFile:
        json.dump(ls, jsonFile)

def csv_to_json(csvName: str, jsonName: str) -> None:
    '''
    @brief Directly converts a cvs file into a json file
    @param csvName: str - name of csv file
    @param jsonName: str - name of json file
    @return None
    '''
    list_to_json(csv_to_list(csvName), jsonName)
