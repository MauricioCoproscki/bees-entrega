from src import transformation
import os

def test_transform_to_silver():
    output = transformation.transform_to_silver("data/bronze/breweries_sample.json")
    assert os.path.exists(output)
