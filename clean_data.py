import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("titanic.csv")

# Display first 5 rows
print(df.head())

# Check missing values
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Save cleaned data
df.to_csv("cleaned_titanic.csv", index=False)

# Survival count graph
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.show()

print("Project Completed Successfully!")