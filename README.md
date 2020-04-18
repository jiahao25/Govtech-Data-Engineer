## Section 1: Data Pipelines

### Files
- Data processing file: `transform_data.py`
- Processed data: `data_processed.csv`
- DAG (scheduling) file: `scheduling.py`

### Working Steps
#### Firstly, I createed the data processing functions in Python
See `transform_data.py` for the functions used.

#### Next, I start a scheduler instance using a Linux terminal by typing the commands below. Visit localhost:8080 to enable the example DAG.
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
#### Lastly, i created the DAG file to create the schedule patterns (1am).
See `scheduling.py ` for the code.
Make sure to save the Python script as `~/airflow/dags/scheduling.py` and then run the terminal command `python ~/airflow/dags/scheduling.py`. 



## Section 2: Databases
Entity Relationship Diagram
![Entity Relationship Diagram](https://raw.githubusercontent.com/jiahao25/Govtech-Data-Engineer-Test/master/images/Entity%20relationship%20diagram%203.JPG "Entity Relationship Diagram")

#### Firstly, i write the SQL file to create the fields and the relationship between the tables.
See `carDealership.sql`

#### Next is to create a Dockerfile for the building of the image. See the code below.
```
#pull base image
FROM postgres
MAINTAINER jiahao

#set environmental variables
ENV POSTGRES_PASSWORD postgres

# copy sql file. the sql file will be run when the container runs.
COPY carDealership.sql /docker-entrypoint-initdb.d/
```

#### After the Dockerfile is written, build the image and launch the container.
Step 1: Build the image where the Dockerfile lies using the terminal command `docker build -t [imagename] .`

Step 2: Run the container using the command `$ docker run -d --name [containername] -p [internal_port]:5432 [imagename]`.



## Section 3: System Design

The following diagram shows the data infrastructure of the company operations on Google Cloud Platform.
![](https://raw.githubusercontent.com/jiahao25/Govtech-Data-Engineer-Test/master/images/architecture.JPG "Data infrastructure")

The services are categorized into 4 categories.
- Red: Non-streaming services
- Green: Streaming services
- Yellow: Connectors, usually data warehouses and databases
- Grey: Data batch services, such as HDFS Solutions

Most services have both Producer and Consumer applications, as denoted by their double arrow.

Within the Kafka Cluster, there are many Topics, each provides different values to the company. I will illustrate the design of one Topic (Business Intelligence).

![](https://raw.githubusercontent.com/jiahao25/Govtech-Data-Engineer-Test/master/images/BItopic.JPG "Business Intelligence topic within Kafka Cluster")


The diagram shows 4 categories and we can connect these apps/processes into the respective Kafka APIs:
- Red: Producers
- Green: Stream Processes
- Yellow: Connectors
- Grey: Consumers

In this example (Business Intelligence topic),

The web app serves as the producers as it publishes a stream of image metadata to the topic for analysis purposes.

Meanwhile, the web app (stream processes) will monitor the user's real time actions such as number of clicks on the site, time spent on the site etc. 

The connectors (databases) will keep update their values as changes are captured on images and user activities

Lastly, the consumer applications will process the records and do analysis. Real time analytics applications will run on real time while BigQuery may run on a designated time period (eg: once a day).

With this diagram, it highlights one main benefit of the Kafka cluster which is a distributed system.
