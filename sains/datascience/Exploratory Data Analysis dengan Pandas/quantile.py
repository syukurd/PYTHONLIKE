import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

Q1 = order_df[["product_weight_gram"]].quantile(0.25)
Q3 = order_df[["product_weight_gram"]].quantile(0.75)

IQR = Q3-Q1
print(IQR)


# Ganti nama kolom freight_value menjadi shipping_cost
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
print(order_df)