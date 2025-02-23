#todo reading (.txt, .json, .csv)

# import os
# import json
import csv
file_path = "test.csv"

# try:
#     with open(file_path, "r") as file:
#         txt = file.read()
#     print(txt)
# except FileNotFoundError:
#     print(f"File '{file_path}' not found.")

# try:
#     with open(file_path, "r") as file:
#         txt = json.load(file)
#         print(txt)
# except FileNotFoundError:
#     print(f"File '{file_path}' not found.")
# except JSONDecodeError:
#     print(f"File '{file_path}' is not a valid JSON file.")

try:
    with open(file_path, "r") as file:
        txt = csv.reader(file)
        for row in txt:
            print(row)
        print(txt)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")



