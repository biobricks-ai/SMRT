# PURPOSE: CHANGE THE DOWNLOADED DATA TO ONE OR MORE PARQUET FILES
import os, shutil, zipfile, pandas as pd

# exports to the ./brick directory
os.makedirs('brick', exist_ok=True)

# make a temp directory
os.makedirs('temp', exist_ok=True)

# unzip the download/smrt_data.zip to temp directory
with zipfile.ZipFile('download/smrt_data.zip', 'r') as zip_ref:
    zip_ref.extractall('temp')

# transform SMRT_DATA to PARQUET
smrt_datset = pd.read_csv('temp/SMRT_dataset.csv',sep=';')
smrt_datset.to_parquet('brick/smrt_dataset.parquet')

# skip other assets which are all generated or redundant to this raw data
# remove temp directory
shutil.rmtree('temp')