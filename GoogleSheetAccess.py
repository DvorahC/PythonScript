from typing import List

import gspread
from oauth2client.service_account import ServiceAccountCredentials
# in order to have nicer print in the console import pprint
from pprint import pprint

'''''''''''''''
1 - This script imports datas from a Google sheet and print it into a console
Defining the access to the Google Sheet
We need a credentials.json in order to get access to the google sheet 
'''''''''''''''

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

client = gspread.authorize(credentials)

sheet = client.open("pythonGoogleSheet").sheet1

data = sheet.get_all_records()

pprint(data)
