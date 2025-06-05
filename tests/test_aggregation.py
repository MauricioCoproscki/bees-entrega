from src import aggregation
import os

def test_aggregate_data():
    output = aggregation.aggregate_data()
    assert os.path.exists("data/gold/brewery_aggregates.parquet")
