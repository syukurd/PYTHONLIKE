import matplotlib.pyplot as plt
import datetime
import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['CMV'] = dataset['item_price'] * dataset['quantity']
print(dataset.head())
plt.figure(figsize=(15,5))
a=dataset.groupby(['order_month'])['CMV'].sum().plot(linestyle='-.',marker='o')
plt.title('Hello Dunia')
plt.xlabel('Order_month', fontsize=12)
plt.ylabel('Order_month', fontsize = 12) 

plt.show()