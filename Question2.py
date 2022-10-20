import pandas as pd
#Read 'data.csv'.
df = pd.read_csv("data.csv")
print(df.describe())
print(df.info())
print(df.isnull().values.any())
print(df.isnull().sum())
df['Calories'].fillna(value=df['Calories'].mean(), inplace=True)
print(df)
print(df.isnull().values.any())
dff = df[["Pulse","Calories"]].min()
df.groupby(["Duration","Pulse"]).agg(['min', 'max', 'count', 'mean'])
df[((df["Calories"]>500) & (df["Calories"]<1000))]
df[((df["Calories"]>500) | (df["Calories"]<100))]
df_modified = df.loc[:, df.columns != 'Maxpulse']
df_modified
df.drop(["Maxpulse"],axis=1,inplace=True)
df
df["Calories"] = df["Calories"].astype(int)
df.info()
df.plot.scatter(x="Duration",y="Calories")