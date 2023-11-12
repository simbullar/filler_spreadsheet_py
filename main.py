from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread
import os

with open("something.txt", "w") as f:
    f.write('')
    f.close
spreadsheet_id = "YOUR_SPREADSHEET_ID"

creds = service_account.Credentials.from_service_account_file("key.json", scopes=["https://www.googleapis.com/auth/spreadsheets", 'https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'])

client = gspread.authorize(creds)

sheet = client.open_by_key(spreadsheet_id)

sheet_instance = sheet.get_worksheet(0)

def get_last_n_characters(text, n):
    last_n_characters=text[-n:]
    return last_n_characters

def colnum_string(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string
#? 

def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def find_lines_containing_any(filename, wanted):
    with open(filename, 'r') as dna_file:
       for dna_line in dna_file:
            if wanted in dna_line:
                yield dna_line
#?
value = sheet_instance.col_values(col=2)
print(value)
f = open("something.txt", "a")
for x in range(len(value)):
    f.write(value[x]+"\n")
f.close

smth = "bc:32:5f:e9:93:01"
for dna in find_lines_containing_any('something.txt', smth):
    print(dna)
#! 11    
#f = open("something.txt", "a")
#i = 1
#for file in get_files(r'C:\Users\simbullar\Documents\python\sheet\files'):
#    one = file[-1]
#    b = open("C:\\Users\\simbullar\\Documents\\python\\sheet\\files\\"+file, "r")
#   for line in b:
#      last = get_last_n_characters(line, 2)
#        cell = sheet_instance.find(query=(line[:-2]).replace(" ", ""), in_column=2)
#        print((line[:-2]).replace(" ", ""))
#        try:
#            row = cell.row
#            range_s = ("%s%s" % ("D", row))
#            sheet_instance.update(range_name=range_s, values="sw"+one+"_"+str(last))
#        except AttributeError:
#            print("None")