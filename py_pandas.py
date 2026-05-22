import pandas as pd

df = pd.read_csv('details.csv')
# print(df)
# new_df = df.dropna()
# print(new_df.to_string())
# df.fillna({"Calories": 130}, inplace=True)
# print(df)

df['Date'] = pd.to_datetime(df['Date'], format = 'mixed')
df.dropna(subset=['Date'], inplace=True)

# df.loc[7, 'Duration'] = 45
# print(df)

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

df.drop_duplicates(inplace=True)

df.to_csv("filtered_data.csv", index=False)