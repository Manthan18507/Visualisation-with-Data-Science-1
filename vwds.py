import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("country_vaccinations.csv")
df.head(10)
df.isnull().any
subset = df.iloc[:5200, :]
plt.figure(figsize=(12,8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.show()

df.head(10)

# Example: Interpolate numbers first, then backfill any remaining text gaps

clean_data = df.dropna(how="all").copy()

num_cols = clean_data.select_dtypes(include="number").columns

clean_data[num_cols] = clean_data[num_cols].interpolate()

clean_data = clean_data.bfill()

df_dropped = df.dropna()
df_dropped