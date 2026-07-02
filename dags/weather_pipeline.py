from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.main import WeatherETLPipeline

pipeline = WeatherETLPipeline()


def extract():
    return pipeline.extract()


def transform(ti):
    raw_file = ti.xcom_pull(task_ids="extract")
    return pipeline.transform(raw_file)


def load(ti):
    transformed_file = ti.xcom_pull(task_ids="transform")
    pipeline.load(transformed_file)


# with DAG(
#     dag_id="weather_etl_pipeline",
#     start_date=datetime(2025, 1, 1),
#     schedule="@daily",
#     catchup=False,
#     tags=["etl", "weather"],
# ) as dag:

with DAG(
    dag_id="weather_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="*/3 * * * *",
    catchup=False,
    tags=["etl", "weather"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    extract_task >> transform_task >> load_task