import pandas as pd
import numpy as np

order_products_prior_df = pd.read_csv("data/order_products__prior.csv")
products_df = pd.read_csv("data/products.csv")
aisles_df = pd.read_csv("data/aisles.csv")
departments_df = pd.read_csv("data/departments.csv")
orders_df = pd.read_csv("data/orders.csv")

print("orders_df.shape={}".format(orders_df.shape))

orders_df = orders_df[orders_df['eval_set']=='prior']
orders_df.drop(['eval_set', 'order_dow','order_hour_of_day','days_since_prior_order'], axis=1, inplace=True)

print("After dropping columns, orders_df.shape={}".format(orders_df.shape))

order_products_prior_df.drop(['add_to_cart_order', 'reordered'], axis=1, inplace=True)

print("Start merging")
order_products_prior_df = pd.merge(order_products_prior_df, products_df, on='product_id', how='left')
print("Merge of order_products_prior_df and products_df done")
orders_products_users = pd.merge(order_products_prior_df, orders_df, on='order_id', how='left')
print("Merge of the previous result and orders_df done -> orders_products_users")

orders_products_users.to_csv('orders_products_users.csv')

print("orders_products_users.shape={}".format(orders_products_users.shape))