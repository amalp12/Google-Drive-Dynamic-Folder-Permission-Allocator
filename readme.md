# Google Drive Permission Allocator

An Application to create folders for specific emails and share each folder with corresponding email only.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```
## Tweakable Variables
**`CLIENT_SECRET_FILE`** - Path to client_secret.json 

**`API_NAME`** = 'drive'

**`API_VERSION`** = 'v3' 

**`SCOPE`** = ['https://www.googleapis.com/auth/drive'] 

**`PARENT_FOLDER_ID`** - Folder ID of the parent folder in which the subfolders are to be created 

**`CSV_PATH`** = 'data.csv' ( path to csv file )

## Input File Format
**`The CSV File`** : Create a csv file with columns name, roll_no and email without any spelling alterations Take the sample csv file given in the repo as reference

## Usage

Edit and set up the required variables mentioned above

Add `client_secret.json` into this directory

Run
```bash
python Main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Note 
Do not forget to add `client_secret.json` into the current working directory.

## License
[MIT](https://choosealicense.com/licenses/mit/)
