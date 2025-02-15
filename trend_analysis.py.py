import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("interior_design_trends.csv")

# Data Cleaning
df = df.dropna()
df['Style'] = df['Style'].str.lower().str.strip()
df['Color'] = df['Color'].str.lower().str.strip()
df['Popularity Score'] = df['Popularity Score'].astype(int)
df = df.drop_duplicates()

# Analysis - Popular Design Styles
design_trends = df.groupby('Style')['Popularity Score'].mean().sort_values(ascending=False)

# Visualization
plt.figure(figsize=(10,5))
design_trends.plot(kind='bar', color='skyblue')
plt.xlabel("Interior Design Style")
plt.ylabel("Average Popularity Score")
plt.title("Trending Interior Design Styles in 2024")
plt.show()
