from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

def get_google_sheet_service():
    key_path = os.getenv('GOOGLE_SHEET_KEY_PATH')

    credentials = Credentials.from_service_account_file(
        key_path,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    service = build('sheets', 'v4', credentials=credentials)

    return service


def get_data_from_google_sheet(range_name: str):
    service = get_google_sheet_service()
    spreadsheet_id = os.getenv('SHEET_ID')

    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=spreadsheet_id,
        range=range_name
    ).execute()

    values = result.get('values', [])

    return values


def get_admin_from_google_sheet():
    values = get_data_from_google_sheet('계정!A3:B3')
    return values[0]


def get_valid_ad_information_from_google_sheet():
    values = get_data_from_google_sheet('광고매물!A2:Y')

    for i, row in enumerate(values):
        if row[0] == "FALSE":
            return values[:i]

    return values


def get_ad_regist_cost_summary_from_google_sheet():
    values = get_data_from_google_sheet('통계!A2:C')
    return values


def update_last_ad_regist_date(row_index: int):
    service = get_google_sheet_service()
    spreadsheet_id = os.getenv('SHEET_ID')

    today_str = datetime.today().strftime("%Y-%m-%d")
    row_index = row_index + 2

    range_name = f"광고매물!X{row_index}"

    body = {
        "values": [[today_str]]
    }

    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption="RAW",
        body=body
    ).execute()


def update_last_ad_cost_summary():
    service = get_google_sheet_service()
    spreadsheet_id = os.getenv('SHEET_ID')

    today_str = datetime.today().strftime("%Y-%m-%d")
    ad_cost = 1450
    ad_count = 1

    values = get_ad_regist_cost_summary_from_google_sheet()

    row_index = len(values) + 2
    new_cost = ad_cost
    new_count = ad_count

    if values and values[-1][0] == today_str:
        row_index = len(values) + 1
        prev_row = values[-1]
        prev_cost = int(prev_row[1]) if len(prev_row) > 1 and prev_row[1].isdigit() else 0
        prev_count = int(prev_row[2]) if len(prev_row) > 2 and prev_row[2].isdigit() else 0
        new_cost = prev_cost + ad_cost
        new_count = prev_count + ad_count
    else:
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f"통계!A{row_index}",
            valueInputOption="RAW",
            body={"values": [[today_str]]}
        ).execute()

    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=f"통계!B{row_index}",
        valueInputOption="RAW",
        body={"values": [[new_cost]]}
    ).execute()

    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=f"통계!C{row_index}",
        valueInputOption="RAW",
        body={"values": [[new_count]]}
    ).execute()