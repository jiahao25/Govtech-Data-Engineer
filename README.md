## Section 1: Data Pipelines

- Python file: `transform_data.py`
- Processed data: `data_processed.csv`
- DAG file: `scheduling.py`

#### **Instructions**
#### Step 1: Create the data processing functions in Python
See `transform_data.py`

#### Step 2: On a Linux terminal, run the following commands at a chosen directory.
```
# (choose the directory)
export AIRFLOW_HOME=~/airflow

# install from pypi using pip
pip install apache-airflow

# initialize the database
airflow initdb

# start the web server, default port is 8080
airflow webserver -p 8080

# start the scheduler
airflow scheduler
```
Then visit localhost:8080 in the browser to enable the example dag in the home page

#### Step 3: Create DAG file
See `scheduling.py `.

Save the Python script as ~/airflow/dags/scheduling.py .

Then run the command `python ~/airflow/dags/tutorial.py`


### Section 2: Databases
Entity Relationship Diagram
![Entity Relationship Diagram](https://raw.githubusercontent.com/jiahao25/Govtech-Data-Engineer-Test/master/images/entity%20relationship%20diagram.JPG "Entity Relationship Diagram")
Note: modelNameVariant is a unique field that comprises of 2 individual fields, *modelName* and *modelVariant*. The field is created by the concatenation of the 2 fields, for example a car model with model *beetle3* and variant *green* will have the field as *beetle3_green*.

### Section 3: System Design

The following diagram shows the data infrastructure of the company operations on Google Cloud Platform.
![](https://raw.githubusercontent.com/jiahao25/Govtech-Data-Engineer-Test/master/images/architecture.JPG "Data infrastructure")

The services are categorized into 4 categories.
- Red: Non-streaming services
- Green: Streaming services
- Yellow: Connectors, usually data warehouses and databases
- Grey: Data batch services, such as HDFS Solutions

Within the Kafka Cluster, there are many topics. I will illustrate the design of one topic (Business Intelligence).
![](https://raw.githubusercontent.com/jiahao25/Govtech-Data-Engineer-Test/master/images/BItopic.JPG "Business Intelligence topic within Kafka Cluster")


The diagram has 4 categories and we connect these apps/processes into the respective Kafka APIs:
- Red: Producers
- Green: Stream Processes
- Yellow: Connectors
- Grey: Consumers

In this example (Business Intelligence topic),

The web app serves as the producers as it publishes a stream of image metadata to the topic for analysis purposes.

Meanwhile, the web app (stream processes) will monitor the user's real time actions such as number of clicks on the site, time spent on the site etc. 

The connectors (databases) will keep update their values as changes are captured on images and user activities

Lastly, the consumer applications will process the records and do analysis. Real time analytics applications will run on real time while BigQuery may run on a designated time period (eg: once a day).
