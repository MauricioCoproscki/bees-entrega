import pandas as pd
import glob
import os

def aggregate_data(input_dir="data/silver", output_dir="data/gold"):
    os.makedirs(output_dir, exist_ok=True)
    parquet_files = glob.glob(f"{input_dir}/*.parquet")
    df_list = [pd.read_parquet(file) for file in parquet_files]
    df = pd.concat(df_list)
    agg = df.groupby(['state', 'brewery_type']).size().reset_index(name='brewery_count')
    agg.to_parquet(f"{output_dir}/brewery_aggregates.parquet", index=False)
    return agg

if __name__ == "__main__":
    aggregate_data()
