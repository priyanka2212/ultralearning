# -*- coding: utf-8 -*-
"""
This is the dag which will be deployed on cloud composer for running stream jobs
"""

from airflow import DAG
#from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.dataflow_operator import DataflowTemplateOperator
from datetime import datetime, timedelta
#from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook
#from google.cloud import storage
#from airflow.models import Variable

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 8, 10),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG('Stream_Dataflow_dag',
            catchup=False,
            schedule_interval=None,
            default_args=default_args)


start = DummyOperator(task_id='start',dag=dag)

job = DataflowTemplateOperator(
        task_id='template_stream_job',
        template="myfirstproject-gcp-file-source/streamtemplate",
        job_name='job_stream_from_airflow',
        
        dataflow_default_options={
            "project": "evident-airline-426602-r1",
            "stagingLocation": "gs://myfirstproject-gcp-file-source/dataflow/staging",
            "tempLocation": "gs://myfirstproject-gcp-file-source/dataflow/temp",
            "serviceAccountEmail": "demo-3@evident-airline-426602-r1.iam.gserviceaccount.com"},
        #parameters={
         #   "input_subscription": "projects/fabric-1333/subscriptions/gcp-yelp-topic-sub",
          #  "output_table": "test.yelp_covid",
           # "output_error_table": "test.error"           
        #},
                dag=dag)

start >> job

"""with dag:
    start = DummyOperator(task_id='start')
    t1 = PythonOperator(
        task_id='Pipeline_definition',
        python_callable=upload_pipeline_def)

    start >> t1
    """