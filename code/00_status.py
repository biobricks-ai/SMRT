# PURPOSE: CHECK IF THE SOURCE HAS CHANGED
import requests
source_url = "https://figshare.com/articles/dataset/The_METLIN_small_molecule_dataset_for_machine_learning-based_retention_time_prediction/8038913"

# request.get source_url to status.txt
response = requests.get(source_url)

with open("status.txt", "w") as file:
    file.write(str(response.text))