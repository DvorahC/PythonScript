import glob
import re
from prettytable import PrettyTable
import csv
import sys


'''''''''''''''
This script:
gather datas from a java folder, using regex and sorting them out
prints the data into a specific csv file
print the data into the console  
'''''''''''''''

'''''''''''''''
1 - Getting the data from the Java file 
'''''''''''''''
path_to_features = sys.argv[2]

#path_to_features = "C:\\Users\\wishtrip\\IdeaProjects\\java-ui-automation-mobile\\src\\test\\java\\cucumber\\features\\*.feature"
files_path = glob.glob(path_to_features)
x = PrettyTable()
x.field_names = ["File", "Feature", "Scenario", "Tags"]

'''''''''''''''
2 - importing the data into the csv file AND printing into the console
'''''''''''''''


def create_csv_file():
    for files_to_target in files_path:
        file_name = re.search(r"(\w*\.feature)", files_to_target).group(1)
        with open(files_to_target, "r") as f:
            file_str = f.read()
            feature_name = re.search(r'(Feature:.*)\S*', file_str).group(1)
            tags_and_scenario = re.findall(r"(@.*\S*\s*)(Scenario:.*\S*)", file_str)
            for elem in tags_and_scenario:
                tags, scenario = elem
                tags_without_space = tags.strip()
                data_to_scv = [file_name, feature_name, scenario, tags_without_space]
                with open('all_scenarios.csv', 'a', newline='') as csvFile:
                    writer = csv.writer(csvFile, delimiter=',', quotechar='`')
                    writer.writerow(data_to_scv)


def create_table_in_console():
    for files_to_target in files_path:
        file_name = re.search(r"(\w*\.feature)", files_to_target).group(1)
        with open(files_to_target, "r") as f:
            file_str = f.read()
            feature_name = re.search(r'(Feature:.*)\S*', file_str).group(1)
            tags_and_scenario = re.findall(r"(@.*\S*\s*)(Scenario:.*\S*)", file_str)
            for elem in tags_and_scenario:
                tags, scenario = elem
                x.add_row([file_name, feature_name, scenario, tags])
                x.align["File"] = "l"
                x.align["Feature"] = "l"
                x.align["Scenario"] = "l"
                x.align["Tags"] = "l"
    print(x)


user_answer = sys.argv[1]

'''''''''
user_answer = input(
            'This program will get you an updated report of all the files, scenario and tags available.\n'
            'to print the report in the console type: CONSOLE \n'
            'to generate all the report in a csv file type: CSV :')
'''''''''

while True:
    if user_answer == 'CONSOLE':
        create_table_in_console()
        break
    elif user_answer == 'CSV':
        with open('all_scenarios.csv', 'a', newline='') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=["FILE", "FEATURE", "SCENARIO", "TAGS"])
            writer.writeheader()
        create_csv_file()
        break
    else:
        user_answer = input(' wrong answer. Please enter CONSOLE or CSV : ')
        continue

