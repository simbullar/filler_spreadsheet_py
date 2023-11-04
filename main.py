from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread

spreadsheet_id = "YOUR_SPREADSHEET_ID"

creds = service_account.Credentials.from_service_account_file("key.json", scopes=["https://www.googleapis.com/auth/spreadsheets", 'https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'])

client = gspread.authorize(creds)

sheet = client.open('YOUR_SPREADSHEET_NAME')

sheet_instance = sheet.get_worksheet(0)

def get_last_n_characters(text, n):
    last_n_characters=text[-n:]
    return last_n_characters


f = open("something.txt", "r")
i = 1
for line in f:
    i = i + 1
    last = get_last_n_characters(line, 2)
    need_to_write = "sw1-" + last
    print(need_to_write)
    cell = sheet_instance.cell(col=4, row=i)
    cell.fill(line)
