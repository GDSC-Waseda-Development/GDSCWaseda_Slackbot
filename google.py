from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

creds = Credentials.from_authorized_user_file('.token')

service = build('docs', 'v1', credentials=creds)

# The testing doc's id
document_id = '1f9J_DlkHBnFOKhLwVj58J0fiEK48LMD8IyArq0CkIHc'

# Define the requests for adding text
requests = [
    {
        'insertText': {
            'location': {
                'index': 1,
            },
            'text': 'Text to be added from python using doc api.'
        }
    }
]

# Execute the requests
result = service.documents().batchUpdate(
    documentId=document_id, body={'requests': requests}).execute()

print('The document has been updated.')

