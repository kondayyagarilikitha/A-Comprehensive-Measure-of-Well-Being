import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/hdi_clean.csv")

# 1. HDI Distribution
plt.figure()
sns.histplot(df["Human Development Index (2021)"])
plt.title("HDI Distribution")
plt.savefig("static/charts/hdi_distribution.png")

# 2. Life Expectancy vs HDI
plt.figure()
sns.scatterplot(
    x=df["Life Expectancy at Birth (2021)"],
    y=df["Human Development Index (2021)"]
)
plt.title("Life Expectancy vs HDI")
plt.savefig("static/charts/life_vs_hdi.png")

# 3. GNI vs HDI
plt.figure()
sns.scatterplot(
    x=df["Gross National Income Per Capita (2021)"],
    y=df["Human Development Index (2021)"]
)
plt.title("GNI vs HDI")
plt.savefig("static/charts/gni_vs_hdi.png")

print("Charts generated successfully")