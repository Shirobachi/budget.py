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