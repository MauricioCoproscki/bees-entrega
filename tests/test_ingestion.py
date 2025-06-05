from src import ingestion

def test_fetch_breweries():
    data = ingestion.fetch_breweries()
    assert isinstance(data, list)
    assert 'id' in data[0]
