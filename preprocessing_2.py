import pandas as pd

print("Start reading file")
orders_products_users = pd.read_csv("orders_products_users.csv")
print("End")

orders_products_users_1 = orders_products_users[["aisle_id","user_id"]]
print("orders_products_users_1.shape={}".format(orders_products_users_1.shape))

orders_products_users_1 = orders_products_users_1.drop_duplicates()
print("orders_products_users_1.shape={}".format(orders_products_users_1.shape))

users_aisles = pd.crosstab(orders_products_users_1['user_id'], orders_products_users_1['aisle_id'])
users_aisles.to_csv("users_aisles.csv")