import pandas as pd

#load dataset
def load_dataset(dataset):
	df = pd.read_csv(dataset)
	return df

if __name__ == '__main__':
	dataset = 'dataset.csv'
	result = load_dataset(dataset)
	print(result)

