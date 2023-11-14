from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread
import os

with open("something.txt", "w") as f:
    f.write('')
    f.close

def create_instance(id, file_name):
    creds = service_account.Credentials.from_service_account_file(file_name, scopes=["https://www.googleapis.com/auth/spreadsheets", 'https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'])
    client = gspread.authorize(creds)
    sheet = client.open_by_key(id)
    sheet_instance = sheet.get_worksheet(0)
    return sheet_instance

spreadsheet_id = "YOUR_SPREADSHEET_ID"

sheet_instance = create_instance(spreadsheet_id, "key.json")
sheet_instance2 = create_instance(spreadsheet_id, "key2.json")
#? START OF FUNCTIONS

def get_last_n_characters(text, n):
    last_n_characters=text[-n:]
    return last_n_characters

def colnum_string(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string


def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def get_num_of_smth(list, value):
    i = 0
    for item in list:
        if item == value:
            return i + 1
        else:
            i = i + 1
#? END OF FUNCTIONS

value = sheet_instance.col_values(col=2)

for file in get_files(r'C:\Users\simbullar\Documents\python\sheet\files'):
    one = file[-1]
    b = open("C:\\Users\\simbullar\\Documents\\python\\sheet\\files\\"+file, "r")
    for line in b:
        line_num = get_num_of_smth(value, line[:-2].replace(" ", ""))
        print((line[:-2]).replace(" ", ""))
        if line_num != None:
            last = get_last_n_characters(line, 2)
            range_s = ("%s%s" % ("D", line_num))
            try:
                sheet_instance.update(range_name=range_s, values="sw"+one+"_"+str(last))
            except gspread.exceptions.APIError:
                sheet_instance2.update(range_name=range_s, values="sw"+one+"_"+str(last))
        elif line_num == None:
            print("None")