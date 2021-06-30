from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Pbp0chgXpH6sJwPCyUa_k2FM_teuSslRHmpgN-c_LdY'


service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
sheet = service.spreadsheets()

def getSheet():
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="List of products for reviews!A2:D27").execute()
    values = result.get('values', [])
    #print(values)
    return values

def getEmails():
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Fourreasons.us!A2:L10").execute()
    values = result.get('values', [])
    #print(values)
    return values
    
def writeSheet(values,index):
    enviar = sheet.values().update(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f"Fourreasons.us!{index}", valueInputOption="USER_ENTERED", body={"values":values}).execute()
    print(enviar)
#print(getSheet())
#writeSheet([['Succes']], "O3")
##print(getEmails())