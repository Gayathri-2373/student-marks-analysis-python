import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("marks.csv")

print("Student Marks Data:\n", data)

# Calculate average marks
data["Average"] = data[["Math", "Science", "English"]].mean(axis=1)

print("\nAverage Marks:\n", data[["Name", "Average"]])

# Highest scorer
highest = data.loc[data["Average"].idxmax()]
print("\nHighest Scorer:\n", highest)

# Plot average marks
plt.bar(data["Name"], data["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Average Marks of Students")
plt.show()
