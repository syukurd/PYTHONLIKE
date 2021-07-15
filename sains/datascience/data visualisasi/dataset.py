import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
print('%d baris dan %d kolom \n' % dataset.shape)
print(dataset.head())