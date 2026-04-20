import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("students.csv")

print("Dataset Loaded:\n")
print(df.head())

# -----------------------------
# 2. Create Average Marks Column
# -----------------------------
df['average_marks'] = (df['math'] + df['science'] + df['programming']) / 3

print("\nDataset with Average Marks:\n")
print(df)

# -----------------------------
# 3. Top Performing Student
# -----------------------------
top_student = df.loc[df['average_marks'].idxmax()]

print("\nTop Performing Student:")
print(top_student)

# -----------------------------
# 4. Department-wise Average
# -----------------------------
dept_avg = df.groupby('department')['average_marks'].mean()

print("\nDepartment-wise Average Marks:")
print(dept_avg)

# -----------------------------
# 5. At-Risk Students
# -----------------------------
at_risk = df[(df['average_marks'] < 60) | (df['attendance'] < 75)]

print("\nAt-Risk Students:")
print(at_risk)

# -----------------------------
# 6. Overall Class Average
# -----------------------------
overall_avg = df['average_marks'].mean()

print("\nOverall Class Average:", overall_avg)

# -----------------------------
# 7. Correlation (Attendance vs Marks)
# -----------------------------
correlation = df['attendance'].corr(df['average_marks'])

print("\nCorrelation between Attendance and Marks:", correlation)

# -----------------------------
# 8. Visualization
# -----------------------------

# Bar Chart: Student vs Average Marks
plt.figure()
plt.bar(df['name'], df['average_marks'])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Column Chart: Department Performance
plt.figure()
dept_avg.plot(kind='bar')
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.title("Department-wise Performance")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Scatter Plot: Attendance vs Marks
plt.figure()
plt.scatter(df['attendance'], df['average_marks'])
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.title("Attendance vs Marks")
plt.tight_layout()
plt.show()

