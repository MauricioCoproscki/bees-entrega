import requests
import os
import json
from datetime import datetime

def fetch_breweries():
    url = "https://api.openbrewerydb.org/v1/breweries"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    return response.json()

def save_raw_data(data, output_dir="data/bronze"):
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{output_dir}/breweries_{datetime.now().strftime('%Y%m%d')}.json"
    with open(filename, 'w') as f:
        json.dump(data, f)
    return filename

if __name__ == "__main__":
    data = fetch_breweries()
    save_raw_data(data)
