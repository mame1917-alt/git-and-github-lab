import pandas as pandas
df = pd.read_csv("data.csv")
print("N rows:",len(df))
print("Mean sale: ", df["amount"].mean())
print("Largest sale: ", df["amount"].max())