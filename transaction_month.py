import pandas as pd
import numpy as np
import pdb
from datetime import date

data = pd.read_csv("/home/anjana/Desktop/short.csv", encoding="latin-1")
data["transaction_cost"] = data["selling_price"] * data["qty_shipped"]
data["date_shipped"] = pd.to_datetime(data["date_shipped"], format="%Y-%m-%d")

group_by_monthyear = data.groupby(
    ["customer_num", data["date_shipped"].dt.strftime("%Y%m")]
)

sum_monthyear = group_by_monthyear.sum()

top6_sum = sum_monthyear.groupby("customer_num").head(6)
top6_sum = top6_sum.drop(["item_num", "order_num", "selling_price"], axis=1)
top6_sum.rename(columns={"qty_shipped": "transaction_size"}, inplace=True)
top6_sum.to_csv("transaction_month.csv")
pdb.set_trace()
""" df_max = data.groupby(["customer_num"], as_index=False)["date_shipped"].max()
df_min = data.groupby(["customer_num"], as_index=False)["date_shipped"].min()
df_max.rename(columns={"date_shipped": "last_order_date"}, inplace=True)
df_min.rename(columns={"date_shipped": "first_order_date"}, inplace=True)
final_df = pd.merge(df_max, df_min, how="left", on=["customer_num"]) """
# final_df["gap days"] = final_df["last_order_date"] - final_df["first_order_date"]
