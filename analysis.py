import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

print("Dataset Loaded:\n")
print(df.head())

df['average_marks'] = (df['math'] + df['science'] + df['programming']) / 3

print("\nDataset with Average Marks:\n")
print(df)

top_student = df.loc[df['average_marks'].idxmax()]

print("\nTop Performing Student:")
print(top_student)

dept_avg = df.groupby('department')['average_marks'].mean()

print("\nDepartment-wise Average Marks:")
print(dept_avg)

at_risk = df[(df['average_marks'] < 60) | (df['attendance'] < 75)]

print("\nAt-Risk Students:")
print(at_risk)

overall_avg = df['average_marks'].mean()

print("\nOverall Class Average:", overall_avg)

correlation = df['attendance'].corr(df['average_marks'])

print("\nCorrelation between Attendance and Marks:", correlation)

plt.figure()
plt.bar(df['name'], df['average_marks'])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
dept_avg.plot(kind='bar')
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.title("Department-wise Performance")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

plt.figure()
plt.scatter(df['attendance'], df['average_marks'])
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.title("Attendance vs Marks")
plt.tight_layout()
plt.show()

