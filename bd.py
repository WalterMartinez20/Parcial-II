import mysql.connector as db
import json


with open('keys.json') as json_file:
    keys = json.load(json_file)

def convertToBinaryData(filename):
    # Convert digital data to binary format
    try:
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    except:
        return 0