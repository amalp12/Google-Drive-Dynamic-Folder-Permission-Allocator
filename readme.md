An Application to Share Specific Gdrive folders to people only with from a csv file containing their emails for AI CLUB NITC

Note: Do not forget to add client_secret.json into this directory

Variables:

CLIENT_SECRET_FILE - Path to client_secret.json
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']
PARENT_FOLDER_ID - Folder ID of the parent folder in which the subfolders are to be created
CSV_PATH = 'data.csv' # path to csv file

CSV File :
Create a csv file with columns name, roll_no and email  without any spelling alterations
Take the sample csv file given in the repo as reference