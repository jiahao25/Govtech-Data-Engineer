import pandas as pd
import numpy as np

#load dataset
def load_dataset(dataset):
	df = pd.read_csv(dataset)
	return df

def transform_df(df):

	# drop rows with no name
	df.dropna(axis='index',how='all',subset=['name'])

	# add first_name and last_name
	df['first_name']= df['name'].str.split().str[0] 
	df['last_name'] = df['name'].str.split().str[1]
	df.drop(columns='name',inplace=True)

	# remove leading zeros
	df['price'] = df['price'].astype(str).str.lstrip('0')
	df['price'] = pd.to_numeric(df['price'])

	# add new field, above_100
	df['above_100'] = df['price'].apply(lambda x: True if x>100 else False)

	# reorder columns
	df_new = df[['first_name','last_name','price','above_100']]

	#print(df.info())
	#print(df)

	return df_new

def save_data(df):
	df.to_csv('data_processed.csv')

if __name__ == '__main__':
	dataset = 'dataset.csv'
	df = load_dataset(dataset)
	df_new = transform_df(df)
	save_data(df_new)


