from airflow import DAG
from datetime import timedelta

from airflow.models import Variable
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from docker.types import Mount


DATA_DIR = Variable.get('DATA_DIR')

default_args = {
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


with DAG(
    'daily',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2023, 5, 9)
) as dag:
    daily = DockerOperator(
        image='airflow-daily',
        command='--output-dir /data/raw/{{ ds }}',
        network_mode='bridge',
        task_id='docker-airflow-daily',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=DATA_DIR, target='/data', type='bind')]
    )

    pie = DockerOperator(
        image='airflow-daily-graph',
        command='--output-dir /data/raw/{{ ds }}',
        network_mode='bridge',
        task_id='docker-airflow-daily-pie',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=DATA_DIR, target='/data', type='bind')]
    )

    daily >> pie