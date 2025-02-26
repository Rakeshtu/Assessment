from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import json
import os

# OSV API Endpoint
OSV_URL = "https://api.osv.dev/v1/query"
DATA_DIR = "/opt/airflow/data"

# Function to fetch OSV data
def fetch_osv_data():
    headers = {"Content-Type": "application/json"}
    query = {
        "ecosystem": "PyPI",
        "last_modified_since": "2023-01-01T00:00:00Z"
    }
    response = requests.post(OSV_URL, headers=headers, json=query)
    
    if response.status_code == 200:
        os.makedirs(DATA_DIR, exist_ok=True)
        file_path = os.path.join(DATA_DIR, "osv_data.json")
        with open(file_path, "w") as file:
            json.dump(response.json(), file)
        print(f"Data saved to {file_path}")
    else:
        raise Exception(f"Failed to fetch data: {response.text}")

# Airflow DAG definition
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 2, 26),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "osv_data_ingestion",
    default_args=default_args,
    description="Fetches OSV vulnerability data daily",
    schedule_interval="@daily",
)

fetch_task = PythonOperator(
    task_id="fetch_osv_data",
    python_callable=fetch_osv_data,
    dag=dag,
)

fetch_task
