# src/analysis.py

def calculate_metrics(df):
    total = len(df)
    avg_satisfaction = df["Satisfaction"].mean()
    top_tool = df["Preferred Tool"].mode()[0]

    return total, avg_satisfaction, top_tool


def tool_distribution(df):
    counts = df["Preferred Tool"].value_counts()
    percent = df["Preferred Tool"].value_counts(normalize=True) * 100

    return counts, percent