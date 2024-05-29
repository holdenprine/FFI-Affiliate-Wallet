from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Google sheets API Set up
SERVICE_ACCOUNT_FILE = 'Path/to/credentials.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = 'spreadsheet_id'
RANGE_NAME = 'range'

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

def get_coupon():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID)
    values = result.get('values', [])
    # this may need a change depending on range and where coupons and names are stored
    return {row[0]: row[1] for row in values}

def validate_coupon(code):
    coupons = get_coupons()
    return coupons.get(code)
