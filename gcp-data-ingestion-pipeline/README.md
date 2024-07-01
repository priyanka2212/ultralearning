### GCP Services and Engineering Process Implemented
<img src="https://github.com/priyanka2212/ultralearning/blob/main/gcp-data-ingestion-pipeline/GCP%20Data%20Engineering%20Architecture%20Diagram.png" alt="GCP Data Engineering Architecture Diagram" width="750" height="600" />

#### Services

- **Google Cloud Storage (GCS):** Object storage service on GCP
- **Virtual Machine (VM):** Computer instance providing compute resources
- **Cloud Pub/sub:** Data asynchronous streaming service
- **Dataflow:** Batch and stream data processing engine
- **Apache Beam:** Open source programming model for batch and stream data pipeline
- **BigQuery:** Data warehouse for structured datasets
- **Cloud Composer:** Workflow orchestration based on Airflow
- **Airflow:** Open source platform for scheduling and monitoring data pipelines
- **Looker Studio:** Data visualization

#### Engineering Process Implemented

1. **Google Cloud Storage (GCS)**
   - Creating buckets
   - Setting IAM principles/roles
   - Uploading/accessing files in buckets
     ![GCS Source Data Stream - yelpdataset](https://github.com/priyanka2212/ultralearning/blob/main/gcp-data-ingestion-pipeline/images/GCS-Sourcedata-Stream-yelpdatasetjson.JPG)
     
     ![GCS Source Data Stream - businessjsondataset](https://github.com/priyanka2212/ultralearning/blob/main/gcp-data-ingestion-pipeline/images/GCS-Sourcedata-Batch-businessjson.JPG)

2. **Spinning up Virtual Machine (VM) Instance**
   - Creating service account and setting Google application credentials to programmatically access and run scripts/services from VM
   - Creating virtual environment
   - Installing Python, Apache Beam [gcp]

3. **Data Ingestion**
   - **Streaming Data using Pub/Sub, Apache Beam Dataflow, BigQuery**
     - Create Pub/Sub topic and subscription
     ![pubsub subscription](https://github.com/priyanka2212/ultralearning/blob/main/gcp-data-ingestion-pipeline/images/pubsub%20subscription.JPG)
     - Construct Python script to:
       1. Publish streaming JSON messages in Pub/Sub topic
       2. Read JSON messages from Pub/Sub, transform message data, and write results to BigQuery
     - Run and monitor Dataflow job in GCP Console
       ![Dataflow stream job](https://github.com/priyanka2212/ultralearning/blob/main/gcp-data-ingestion-pipeline/images/Dataflow%20-%20stream-job.png)
     - Inspect data in BigQuery
     -  ![Bigquery - stream data output](https://github.com/priyanka2212/ultralearning/blob/main/gcp-data-ingestion-pipeline/images/Bigquery-streamdata.JPG)
       
   - **Batch Data using GCS, Apache Beam Dataflow, BigQuery**
     - Upload JSON data to GCS
     - Construct Python script to:
       1. Read JSON messages from GCS file, transform message data, and write results to BigQuery
     - Run and monitor Dataflow job in GCP Console
     - Inspect data in BigQuery
       ![Bigquery - batch data output](https://github.com/priyanka2212/ultralearning/blob/main/gcp-data-ingestion-pipeline/images/Bigquery-batchdata.JPG)
      
4. **Batch Orchestration using Cloud Composer/Airflow**
   - Creating Cloud Composer environment:
     - Kubernetes cluster, GCS bucket for DAG, Airflow Web UI
       ![Cloud composer Env. config](https://github.com/priyanka2212/ultralearning/blob/main/gcp-data-ingestion-pipeline/images/Cloud%20composer%20-%20environment%20config.JPG)
       ![Kubernetes Cluster](https://github.com/priyanka2212/ultralearning/blob/main/gcp-data-ingestion-pipeline/images/Cloud%20composer%20-%20Kube%20cluster.JPG)
       ![Cloud composer airflow job](https://github.com/priyanka2212/ultralearning/blob/main/gcp-data-ingestion-pipeline/images/Cloud%20composer%20-%20Kube%20cluster.JPG) 
   - Creating Batch job template:
     - Execute Dataflow job in template creation mode to generate a reusable template
   - Create DAG and associate the Batch job template with DataflowTemplateOperator
   - Upload the DAG file to GCS bucket for DAG created by Cloud Composer
     ![GCS DAG Bucket](https://github.com/priyanka2212/ultralearning/blob/main/gcp-data-ingestion-pipeline/images/Cloud%20composer-%20DAG%20bucket.JPG) 
   - Login to Airflow Web UI to trigger and track DAG batch job run
   ![Dataflow Airflow batch job](https://github.com/priyanka2212/ultralearning/blob/main/gcp-data-ingestion-pipeline/images/Dataflow-Airflow-batch_job.JPG) 
   ![Dataflow Airflow batch job](https://github.com/priyanka2212/ultralearning/blob/main/gcp-data-ingestion-pipeline/images/Dataflow-Airflow-batch_job.JPG) 

5. **Inspect Data Loaded in BigQuery and Looker Studio**
   - Query data from BigQuery dataset and understand query estimates
   - Display data results using Looker Studio and simple charts
