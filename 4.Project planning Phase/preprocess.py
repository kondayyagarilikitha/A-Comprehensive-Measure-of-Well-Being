import pandas as pd

df = pd.read_csv("data/hdi.csv")

# Select only required features (IMPORTANT FOR SMARTBRIDGE)
df = df[[
    "Life expectancy",
    "Expected years of schooling",
    "Mean years of schooling",
    "Gross national income (GNI) per capita",
    "Human Development Index (HDI)"
]]

# Handle missing values
df = df.dropna()

# Rename columns (clean format)
df.columns = ["life", "school_exp", "school_mean", "gni", "hdi"]

# Save cleaned dataset
df.to_csv("data/hdi_clean.csv", index=False)

print("Preprocessing completed successfully!")