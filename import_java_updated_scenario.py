import glob
import re
from prettytable import PrettyTable
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

name = os.environ['FILE_NAME']
'''''''''''''''
1 - get Data from a folder and print them into a google sheet/ or into the 
console with pprint 
'''''''''''''''


path_to_features = "C:\\Users\\wishtrip\\IdeaProjects\\java-ui-automation-mobile\\src\\test\\java\\cucumber\\features\\*.feature"


'''''''''''''''
1 - Defining the access to the Google Sheet
'''''''''''''''

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

client = gspread.authorize(credentials)

sheet = client.open("pythonGoogleSheet").sheet1
data = sheet.get_all_records()
#pprint(data)

'''''''''''''''
2 - Getting the data from the Java file 
'''''''''''''''

files_path = glob.glob(path_to_features)

x = PrettyTable()
x.field_names = ["File", "Feature", "Scenario", "Tags"]

'''''''''''''''
2 - importing the data into the spread sheet
'''''''''''''''
#sheet.insert_row(x.field_names, 1)

scenarios = []
for files_to_target in files_path:
    file_name = re.search(r"(\w*\.feature)", files_to_target).group(1)
    with open(files_to_target, "r") as f:
        file_str = f.read()
        feature_name = re.search(r'(Feature:.*)\S*', file_str).group(1)
        tags_name = re.findall(r'(@.*)\S*', file_str)
        scenario_name = re.findall(r"(Scenario:.*)\S*", file_str)
        tagsAndScenario = re.findall(r"(@.*\S*\s*)(Scenario:.*\S*)", file_str)
        for elem in tagsAndScenario:
            tags, scenario = elem
            tagsWithoutSpace = tags.strip()
            x.add_row([file_name, feature_name, scenario, tags])
            #sheet.insert_row([file_name, feature_name, scenario, tagsWithoutSpace], 2)
            sheet.append_row([file_name, feature_name, scenario, tagsWithoutSpace])
            #time.sleep(4)

x.align["File"] = "l"
x.align["Feature"] = "l"
x.align["Scenario"] = "l"
x.align["Tags"] = "l"
print(x)
