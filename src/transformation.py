import pandas as pd
import os
import json

def transform_to_silver(input_path, output_dir="data/silver"):
    os.makedirs(output_dir, exist_ok=True)
    with open(input_path, 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df = df[['id', 'name', 'brewery_type', 'city', 'state', 'country', 'latitude', 'longitude']]
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    for state, group in df.groupby('state'):
        filename = f"{output_dir}/breweries_state={state}.parquet"
        group.to_parquet(filename, index=False)
    return output_dir

if __name__ == "__main__":
    transform_to_silver("data/bronze/breweries_YYYYMMDD.json")
