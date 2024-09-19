from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "faruk3d",
    "retries": 5,
    "retry_delay": timedelta(minutes = 2)
}

def greet():
    print("Hello World!")


with DAG(
    default_args = default_args,
    dag_id = "dag_with_python_operator_v1",
    description = "dag using python operator",
    start_date = datetime(2024, 9, 18),
    schedule_interval = "@daily"
) as dag:
    task1 = PythonOperator(
        task_id = "greet",
        python_callable = greet
    )
    
    task1