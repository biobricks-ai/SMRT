# PURPOSE: DOWNLOAD THE SMRT DATA TO THE ./download DIRECTORY
import os 

# downloads to the ./download directory
os.makedirs('download', exist_ok=True)

# read the data from the ./download directory
import requests
source_url = "https://figshare.com/ndownloader/articles/8038913/versions/1"

# stream the source_url to the ./download/smrt_data.zip
with requests.get(source_url, stream=True) as r:
    r.raise_for_status()
    with open('download/smrt_data.zip', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)