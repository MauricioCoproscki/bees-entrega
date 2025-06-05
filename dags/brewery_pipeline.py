from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from src import ingestion, transformation, aggregation
import os

def get_latest_json():
    files = [f for f in os.listdir('data/bronze') if f.endswith('.json')]
    return 'data/bronze/' + max(files, key=lambda x: os.path.getctime(os.path.join('data/bronze', x)))

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='brewery_pipeline',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    fetch = PythonOperator(
        task_id='fetch_data',
        python_callable=lambda: ingestion.save_raw_data(ingestion.fetch_breweries())
    )

    transform = PythonOperator(
        task_id='transform_data',
        python_callable=lambda: transformation.transform_to_silver(get_latest_json())
    )

    aggregate = PythonOperator(
        task_id='aggregate_data',
        python_callable=aggregation.aggregate_data
    )

    fetch >> transform >> aggregate
