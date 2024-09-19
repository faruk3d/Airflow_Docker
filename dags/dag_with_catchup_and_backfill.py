from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator



default_args = {
    "owner": "faruk3d",
    "retries": 5,
    "retry_delay": timedelta(minutes = 2)
}

with DAG(
    dag_id = "dag_with_catchup_and_backfill_v02",
    default_args = default_args,
    description = "dag with bash operator",
    start_date = datetime(2024, 9, 10),
    schedule_interval = "@daily",
    catchup = False
) as dag:
    task1 = BashOperator(
        task_id = "taks1",
        bash_command = "echo hello world"
    )