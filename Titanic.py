import pandas as pd

df = pd.read_csv("tested.csv")
df = df.drop(columns=["Cabin"])
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())
df.columns = df.columns.str.lower()
df.head()
df.info()
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
df.to_csv("cleaned_titanic.csv", index=False)



