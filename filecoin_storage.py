# filecoin_storage.py
import requests

FILECOIN_API_URL = 'https://api.filecoin.io'  # Replace with actual Filecoin API URL

def upload_file(file_path):
    with open(file_path, 'rb') as file_data:
        response = requests.post(f'{FILECOIN_API_URL}/upload', files={'file': file_data})
        return response.json()

def download_file(file_id, destination_path):
    response = requests.get(f'{FILECOIN_API_URL}/download/{file_id}')
    with open(destination_path, 'wb') as file_data:
        file_data.write(response.content)