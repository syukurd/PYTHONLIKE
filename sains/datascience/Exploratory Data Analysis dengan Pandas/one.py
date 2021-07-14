# import pandas as pd
# order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# print(order_df.shape)


# tampilkan 10 data teratas menggunakan head()
from numpy import median
import pandas as pd
import matplotlib.pyplot as plt
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
print(order_df.head())


# menampilkan summary dari statistic data
print(order_df.describe())

#menampilkan rata rata median dari tabel colom price
print(order_df.loc[:, "price"].median())


#saya mau menampilkan histogram dari price
order_df[["price"]].hist(figsize=(4,5),bins=10,xlabelsize=8,ylabelsize=8)
plt.show()