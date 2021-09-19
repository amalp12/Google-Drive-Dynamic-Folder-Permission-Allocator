from Google import Create_Service
from Google import get_folder_data_from_csv
from Google import get_file_ids
from Google import pd 
CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']
PARENT_FOLDER_ID = '1UNodgQt3hvHlpL1E4_R9BsofAqca5TA0'
CSV_PATH = 'data.csv'
service = Create_Service(CLIENT_SECRET_FILE, API_NAME,API_VERSION, SCOPE)
print(dir(service))


folder_data = get_folder_data_from_csv(CSV_PATH)
for folder in folder_data:
    file_metadata = {
        'name' : folder.name, 
        'mimeType' : 'application/vnd.google-apps.folder',
        'parents' : [PARENT_FOLDER_ID]
    }
    service.files().create(body = file_metadata).execute()


file_ids = get_file_ids(PARENT_FOLDER_ID, service)
file_ids = file_ids.set_index('name')
for folder in folder_data:
    
    
    
    request_body ={
        'role': 'writer',
        'type': 'user',
        'emailAddress' : str(folder.email)
    }
    fileId = str(file_ids['id'][folder.name])
    response_permission = service.permissions().create(
        fileId = fileId,
        body = request_body
    ).execute()
    print(response_permission)