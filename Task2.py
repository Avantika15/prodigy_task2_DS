import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# 1. Load the Titanic dataset
# -----------------------------------

df = pd.read_csv("train.csv")

# Display the first 5 rows
print(df.head())

# Display column names
print(df.columns)

# Display number of rows and columns
print(df.shape)


# -----------------------------------
# 2. Check the data
# -----------------------------------

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())


# -----------------------------------
# 3. Clean the data
# -----------------------------------

# Fill missing Age values with median age
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with the most common value
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove Cabin because most values are missing
df = df.drop("Cabin", axis=1)

# Check missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())


# -----------------------------------
# 4. Survival Distribution
# -----------------------------------

survival = df["Survived"].value_counts()

plt.figure(figsize=(6, 4))
plt.bar(["Did Not Survive", "Survived"], survival)

plt.title("Titanic Survival Distribution", fontweight="bold")
plt.xlabel("Outcome")
plt.ylabel("Number of Passengers")

plt.tight_layout()
plt.savefig("survival_distribution.png")
plt.show()


# -----------------------------------
# 5. Survival by Gender
# -----------------------------------

gender_survival = df.groupby("Sex")["Survived"].sum()

plt.figure(figsize=(6, 4))
plt.bar(gender_survival.index, gender_survival.values)

plt.title("Survival by Gender", fontweight="bold")
plt.xlabel("Gender")
plt.ylabel("Number of Survivors")

plt.tight_layout()
plt.savefig("survival_by_gender.png")
plt.show()


# -----------------------------------
# 6. Survival Rate by Gender
# -----------------------------------

survival_rate = df.groupby("Sex")["Survived"].mean() * 100

plt.figure(figsize=(6, 4))
plt.bar(survival_rate.index, survival_rate.values)

plt.title("Survival Rate by Gender", fontweight="bold")
plt.xlabel("Gender")
plt.ylabel("Survival Rate (%)")

plt.tight_layout()
plt.savefig("survival_rate_by_gender.png")
plt.show()


# -----------------------------------
# 7. Survival Rate by Passenger Class
# -----------------------------------

class_survival = df.groupby("Pclass")["Survived"].mean() * 100

plt.figure(figsize=(6, 4))
plt.bar(class_survival.index, class_survival.values)

plt.title("Survival Rate by Passenger Class", fontweight="bold")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")

plt.tight_layout()
plt.savefig("survival_rate_by_class.png")
plt.show()


# -----------------------------------
# 8. Age Distribution
# -----------------------------------

plt.figure(figsize=(6, 4))
plt.hist(df["Age"], bins=10)

plt.title("Age Distribution of Titanic Passengers", fontweight="bold")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

plt.tight_layout()
plt.savefig("age_distribution.png")
plt.show()



