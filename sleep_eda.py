import pandas as pd

df = pd.read_csv("AutoSleep-20220122-to-20240501.csv")

df.info()

df["ISO8601"].value_counts


df["bedtime"].tail(3)
pd.to_datetime(df["bedtime"].tail(3), infer_datetime_format=True).mean()
df["toDate"] = pd.to_datetime(df["toDate"], infer_datetime_format=True)
df["waketime"] = pd.to_datetime(df["waketime"], infer_datetime_format=True)
df["waketime"] = df["waketime"].dt.time
df["waketime_norm"] = df["waketime"] - df["waketime"].dt.normalize()
df["bedtime_norm"] = df["bedtime"] - df["bedtime"].dt.normalize()
# now for your answer, get the average of the timestamp column
print(df["timestamp"].mean())

df[["toDate", "bedtime"]].groupby(["toDate"].dayofweek).mean()

df[["bedtime", "toDate"]].pivot_table(
    values="count", index=df["toDate"].dayofweek, aggfunc="mean"
)
df_data = df[["bedtime_norm", "toDate", "waketime_norm"]]
week_df = df_data.groupby(df_data["toDate"].dt.weekday).mean()
week_df
