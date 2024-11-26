from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials
from django.conf import settings

def upload_to_drive(file_path, file_name):
    credentials = Credentials.from_service_account_file('credentials.json', scopes=['https://www.googleapis.com/auth/drive'])
    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {
        'name': file_name,
        'parents': [settings.GOOGLE_DRIVE_FOLDER_ID]
    }
    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id, webContentLink').execute()

    return file.get('webContentLink')  # Return the public URL of the uploaded file
