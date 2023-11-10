from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread

spreadsheet_id = "YOUR_SPREADSHEET_ID"

creds = service_account.Credentials.from_service_account_file("key.json", scopes=["https://www.googleapis.com/auth/spreadsheets", 'https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'])

client = gspread.authorize(creds)

sheet = client.open_by_key(spreadsheet_id)

sheet_instance = sheet.get_worksheet(0)

def get_last_n_characters(text, n):
    last_n_characters=text[-n:]
    return last_n_characters


f = open("something.txt", "r")
i = 1
for line in f:
    i = i + 1
    last = get_last_n_characters(line, 2)
    cell = sheet_instance.findall((line[:-2]).replace(" ", ""))
    print((line[:-2]).replace(" ", ""))
    print(cell)
#!    sheet_instance.update(range_name='D' + str(cell), values="sw1-" + str(last))
