import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from pprint import pprint
import string

# Prepairint and connect
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
cred = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
client = gspread.authorize(cred)
sheet = client.open("Expense Tracker").sheet1

print("Script started!")

def show():
    # get all data
    data = sheet.get_all_records()

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


def fillUp():
	data = sheet.get_all_records()

	for i in range(len(data)):
		for index, cell in data[i].items():
			if cell == "":
				if index == "Purchase Date":
					sheet.update_cell(i+2, 2, sheet.cell(i+2-1, 2).value)
				elif index == "Item":
					sheet.update_cell(i+2, 3, sheet.cell(i+2-1, 3).value)
				elif index == "Amount":
					sheet.update_cell(i+2, 4, sheet.cell(i+2-1, 4).value)
				elif index == "Category":
					sheet.update_cell(i+2, 5, sheet.cell(i+2-1, 5).value)
        
		goodFormatted = data[i]["Item"]
		goodFormatted = goodFormatted.lower()
		goodFormatted = goodFormatted.replace(goodFormatted[0], goodFormatted[0].upper(), 1)
        
		if not data[i]["Item"] == goodFormatted:
			sheet.update_cell(i+2, 3, goodFormatted)

show()
fillUp()
show()