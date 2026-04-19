import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# 1. CREATE SYNTHETIC DATA
# ----------------------------
data = {
    "Age Group": np.random.choice(["18-24", "25-34", "35-44"], 100),
    "Gender": np.random.choice(["Male", "Female"], 100),
    "Preferred Tool": np.random.choice(["Python", "Excel", "R"], 100),
    "Satisfaction": np.random.randint(1, 6, 100),
}

df = pd.DataFrame(data)
df.to_csv("data/poll_data.csv", index=False)

# ----------------------------
# 2. LOAD DATA
# ----------------------------
df = pd.read_csv("data/poll_data.csv")

# ----------------------------
# 3. CLEANING
# ----------------------------
df.drop_duplicates(inplace=True)
df["Preferred Tool"] = df["Preferred Tool"].str.strip()

# ----------------------------
# 4. ANALYSIS
# ----------------------------
tool_counts = df["Preferred Tool"].value_counts()
tool_percent = df["Preferred Tool"].value_counts(normalize=True) * 100

print("Vote Count:\n", tool_counts)
print("\nPercentage:\n", tool_percent)

# ----------------------------
# 5. VISUALIZATION
# ----------------------------

# Bar Chart
plt.figure()
sns.countplot(x="Preferred Tool", data=df)
plt.title("Tool Preference")
plt.savefig("outputs/bar_chart.png")

# Pie Chart
tool_counts.plot.pie(autopct='%1.1f%%')
plt.title("Tool Share")
plt.savefig("outputs/pie_chart.png")

# ----------------------------
# 6. INSIGHTS
# ----------------------------
top_tool = tool_counts.idxmax()
print(f"\nMost Preferred Tool: {top_tool}")