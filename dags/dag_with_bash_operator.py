from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator



default_args = {
    "owner": "faruk3d",
    "retries": 5,
    "retry_delay": timedelta(minutes = 2)
}

with DAG(
    dag_id = "dag_with_bash_operator_v06",
    default_args = default_args,
    description = "dag with bash operator",
    start_date = datetime(2024, 9, 18),
    schedule_interval = "@daily"
    ) as dag:
    task1 = BashOperator(
        task_id = "first_task",
        bash_command = "echo hello world"
    )
    
    task2 = BashOperator(
        task_id = "second_task",
        bash_command = "echo This task will running after the task1"
    )
    
    task3 = BashOperator(
        task_id = "third_task",
        bash_command = "echo This task will be running after task1 at the same time as task2"
    )
    
    # Task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    
    # Task dependency method 2
    # task1 >> task2
    # task1 >> task3
    
    # Task dependency method 3
    task1 >> [task2, task3]