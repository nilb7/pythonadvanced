import pandas as pd

import matplotlib.pyplot as plt

#read file and saves in df
df = pd.read_csv('avgIQpercountry.csv')

filteres_df = df[df["Average IQ"]>=100]


filtered_df = filteres_df.sort_values(by="Average IQ", ascending=False)

print(filtered_df)

plt.figure(figsize=(14,8))

bars = plt.bar(filtered_df["Country"], filteres_df["Average IQ"], color="skyblue")

plt.title("Average IQ by Country (IQ>=100)", fontsize=16)



plt.xlabel("Country",fontsize=14)
plt.xlabel("Average IQ",fontsize=14)

plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)

plt.grid(axis="y",linestyle="--",alpha=0.8)

plt.bar_label(bars,fmt="%.2f",fontsize=10,color="black")

plt.tight_layout()
plt.show()
