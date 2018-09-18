import pandas as pd
import numpy as np
import sys

# opening the CSV with the right encoding
df = pd.read_csv("/home/anjana/anjana/csv/combined_transactions.csv")
# df = pd.read_csv('transactions_test.csv')

# print number of rows and data type of each column of the dataframe
print(len(df))
print(df.dtypes)

# for each customer, finding its first order date and last order date, its most common order type, number of orders placed, mean/median between orders
df["sales"] = df["selling_price"] * df["qty_shipped"]

df_sales = (
    df[["customer_num", "order_num", "sales"]]
    .groupby(["order_num", "customer_num"])
    .sum()
)
df_sales.rename(columns={"sales": "average_order_cost"}, inplace=True)
sales_df = pd.merge(df, df_sales, how="left", on=["customer_num", "order_num"])

df_avg = (
    sales_df[["customer_num", "average_order_cost"]].groupby(["customer_num"]).mean()
)

final_df = pd.merge(df, df_avg, how="left", on=["customer_num"])

import pdb

df_qua = (
    df[["customer_num", "order_num", "qty_shipped"]]
    .groupby(["order_num", "customer_num"])
    .sum()
)
df_qua.rename(columns={"qty_shipped": "average_order_size"}, inplace=True)
df_qua_avg = pd.merge(df, df_qua, how="left", on=["customer_num", "order_num"])


df_avg_qua = (
    df_qua_avg[["customer_num", "average_order_size"]].groupby(["customer_num"]).mean()
)

final_df_qua = pd.merge(final_df, df_avg_qua, how="left", on=["customer_num"])


final_df[["customer_num", "average_order_cost"]].to_csv(
    "average_order_cost", index=False
)

final_df_qua[["customer_num", "average_order_cost", "average_order_size"]].to_csv(
    "average_order_quality", index=False
)
# pdb.set_trace()
