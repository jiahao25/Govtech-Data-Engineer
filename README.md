### Section 1: Data Pipelines

- Python file: `transform_data.py`
- Raw data: `dataset.csv`
- Processed data: `data_processed.csv`

##### Step 1: Create the data processing functions in Python using Pandas 

See the python file for the code.

##### Step 2: 

### Section 2: Databases

### Section 1: System Design

The following diagram shows the data infrastructure of the company operations on Google Cloud Platform.

The services are categorized into 4 categories.
Red: Non-streaming services
Green: Streaming services
Yellow: Connectors, usually data warehouses and databases
Grey: Data batch services, such as HDFS Solutions

Within the Kafka Cluster, there are many topics. I will illustrate the design of one topic (Business Intelligence).

The diagram has 4 categories and we connect these apps/processes into the respective Kafka APIs:
Red: Producers
Green: Stream Processes
Yellow: Connectors
Grey: Consumers

In this example (Business Intelligence topic),

The web app serves as the producers as it publishes a stream of image metadata to the topic for analysis purposes.

Meanwhile, the web app (stream processes) will monitor the user's real time actions such as number of clicks on the site, time spent on the site etc. 

The connectors (databases) will keep update their values as changes are captured on images and user activities

Lastly, the consumer applications will process the records and do analysis. Real time analytics applications will run on real time while BigQuery may run on a designated time period (eg: once a day).
