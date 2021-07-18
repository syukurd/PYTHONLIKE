import matplotlib.pyplot as plt
import datetime
import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['CMV'] = dataset['item_price'] * dataset['quantity']
print(dataset.head())
plt.figure(figsize=(15,5))
a=dataset.groupby(['order_month'])['CMV'].sum().plot(linestyle='-.',marker='o',color='green',linewidth =2)
plt.title('Hello Dunia')
plt.xlabel('Order_month', fontsize=12)
plt.ylabel('Order_month', fontsize = 12) 
plt.grid(color = 'darkgray',linewidth = 0.5,linestyle = ':' )
labels,locations = plt.yticks()
plt.yticks(labels,(labels/1000000000).astype(int))
# netralkan batas maksimum dan minimum nilai axis ticks
plt.ylim(ymin = 0)

plt.show()