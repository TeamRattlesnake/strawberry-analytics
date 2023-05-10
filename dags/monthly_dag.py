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
    'monthly',
    default_args=default_args,
    schedule_interval='@monthly',
    start_date=datetime(2023, 5, 8)
) as dag:
    monthly = DockerOperator(
        image='airflow-monthly',
        command='--output-dir /data/raw/{{ ds }}',
        network_mode='bridge',
        task_id='docker-airflow-monthly',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=DATA_DIR, target='/data', type='bind')]
    )

    graph = DockerOperator(
        image='airflow-monthly-graph',
        command='--output-dir /data/raw/{{ ds }}',
        network_mode='bridge',
        task_id='docker-airflow-monthly-graph',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=DATA_DIR, target='/data', type='bind')]
    )

    monthly >> graph