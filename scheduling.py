import pandas as pd
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# set first schedule date on 18th april 2020,1am
default_args = {
    'owner': 'airflow',
    'start_date':datetime(2020,4,18,1),
    'retries': 1, 
    'retry_delay': timedelta(minutes=1), 
    }

# next scheduled time to process file is 1 day from the previous scheduled time
dag = DAG(
	'scheduler',
	default_args=default_args,
	schedule_interval= timedelta(days=1),
)

# create bash command to run the .py file
t1 = BashOperator(
	task_id='bash_task',
	bash_command='python transform_data.py',
	dag=dag,
)


t1





