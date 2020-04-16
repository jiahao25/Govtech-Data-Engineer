### Section 1: Data Pipelines

Python file: `transform_data.py`
Raw data: `dataset.csv`
Processed data: `data_processed.csv`

Firstly, process the data. I will be using Python and Pandas to transform and process the data.

Step 1: Load the dataset

```def load_dataset(dataset):
	df = pd.read_csv(dataset)
	return df```
