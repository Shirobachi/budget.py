import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from pprint import pprint
import random 

# Prepairint and connect
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
cred = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
client = gspread.authorize(cred)
sheet = client.open("Tut").sheet1

print("Script started!")
# Do magic

# READING
# pprint(sheet.get_all_records())

# pprint(sheet.row_values(3))
# pprint(sheet.col_values(2))

# pprint(sheet.cell(3, 2).value)

# sheet.insert_row(["is", "it", "working?"], 4)
# sheet.delete_row(4)

# sheet.update_cell(4, 5, 4)
# sheet.update_cell(4, 6, 5)

# sheet.update_cell(5, 5, "=E4+F4")

# sheet.update_cell(6, 6, len(sheet.get_all_records()))


# now = datetime.datetime.now()

# time = ""
# time += now.month + "/"+ now.day+ "/"+ now.year+ " "+ now.hour+ ":"+ now.minute+ ":"+ now.second

# sheet.update_cell(1, 1, time)

# i = 1

# while True:
#     if sheet.cell(1, 1).value != "":
#         if sheet.cell(1, 1).value.isnumeric():
#             print("work")
#             break

# while True:
#     if sheet.cell(1, 1).value == "":
#         sheet.update_cell(1, 1, "")
#         sheet.update_cell(i, 8, random.randint(0, 99))
#         print("Triggered")
#         i -= -1

# --------------------------------------------------------------------------

def show(data):
    # get all data

    # go through by rows
    for row in data: 
        column = 0

        # go through by row's elements
        for item, value in row.items():
            print(str(value), end="")
            # add | if not last
            if column < 4:
                print("|", end="")
            column += 1
        print("")                    


def fillUp(data):

    i = 2
    for row in data:
        for index, cell in row.items():
            if cell == "":
                if index == "Purchase Date":
                    sheet.update_cell(i, 2, sheet.cell(i-1, 2).value)
                elif index == "Item":
                    sheet.update_cell(i, 3, sheet.cell(i-1, 3).value)
                elif index == "Amount":
                    sheet.update_cell(i, 4, sheet.cell(i-1, 4).value)
                elif index == "Category":
                    sheet.update_cell(i, 5, sheet.cell(i-1, 5).value)

        i += 1


data = sheet.get_all_records()

fillUp(data)
show(data)