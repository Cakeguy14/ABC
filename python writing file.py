#todo python writing files (.txt, .JSON, .csv)

import json
import csv

# text_data = ["a", "b", "c", "d", "e"]
# text_data = { "name": "john",
#               "age":  "12",
#               "work": "banker"
}
# text_data = [["Name", "Age", "work"],
#               ["John", "12", "Banker"],
#               ["Jane", "15", "Engineer"],
#               ["David", "18", "Doctor"]]
file_path = "test.csv"

# try:
#     with open(file_path, "a") as file: #todo we can use w-write, x-overwrite, a-append
#         file.write("\n" + text_data)
#         print("File created successfully!")
# except FileExistsError:
#     print("File already exists.")

# try:
#     with open(file_path, "a") as file: #todo we can use w-write, x-overwrite, a-append
#         for txt in text_data:
#             file.write(txt + " ")
#         print("File created successfully!")
# except FileExistsError:
#     print("File already exists.")
#
# try:
#     with open(file_path, "a") as file: #todo we can use w-write, x-overwrite, a-append
#         json.dump(text_data, file, indent=4)
#         print("File created successfully!")
# except FileExistsError:
#     print("File already exists.")
#
# try:
#     with open(file_path, "w", newline="") as file: #todo we can use w-write, x-overwrite, a-append
#         writer = csv.writer(file)
#         for row in text_data:
#             writer.writerow(row)
#         print("File created successfully!")
# except FileExistsError:
#     print("File already exists.")