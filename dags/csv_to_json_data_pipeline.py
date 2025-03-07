import os
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import pandas as pd

def csvTojson():
    abspath = os.path.abspath(os.getcwd())
    datapath = abspath.replace('dags', 'data/data.csv')
    df = pd.read_csv(datapath)
    for i, r in df.iterrows():
        print(r['name'])
    df.to_json('fromAirflow.JSON', orient='records')

default_args = {
    'owner': 'dinabandhu',
    'start_date': dt.datetime(2025, 2, 23),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG(
    'mycsvdag',
    default_args=default_args,
    schedule_interval=timedelta(minutes=5),
    # '0 * * * *',
) as dag:
    print_starting = BashOperator(
        task_id = 'startingBashOperator',
        bash_command='echo "I am reading the csv now"'
    )
    CSVJSON = PythonOperator(
        task_id = 'convertCSVtoJSONwithPython',
        python_callable=csvTojson
    )

print_starting >> CSVJSON