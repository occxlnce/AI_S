import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the SQLite database
conn = sqlite3.connect('survey.db')

# Read data from the 'responses' table
df = pd.read_sql_query("SELECT * FROM responses", conn)

# Close the database connection
conn.close()

# Create a folder to save the plots
import os
if not os.path.exists('plots'):
    os.makedirs('plots')

# Custom visualizations for each question

# 1. Frequency of AI tools usage
plt.figure(figsize=(10, 6))
sns.countplot(x='usage', data=df, order=['Daily', 'Weekly', 'Monthly', 'Rarely', 'Never'])
plt.title('Frequency of AI Tools Usage')
plt.xlabel('Usage Frequency')
plt.ylabel('Count')
plt.savefig('plots/usage_frequency.png')

# 2. Impact of AI tools on academic performance
plt.figure(figsize=(10, 6))
sns.countplot(x='impact', data=df)
plt.title('Impact of AI Tools on Academic Performance')
plt.xlabel('Impact Rating')
plt.ylabel('Count')
plt.savefig('plots/impact_rating.png')

# 3. Academic marks range since using AI tools
plt.figure(figsize=(10, 6))
sns.countplot(x='marks_range', data=df, order=['50-59', '60-69', '70-79', '80-89', '90-99'])
plt.title('Academic Marks Range Since Using AI Tools')
plt.xlabel('Marks Range')
plt.ylabel('Count')
plt.savefig('plots/marks_range.png')

# 4. Hours per week spent using AI tools
plt.figure(figsize=(10, 6))
sns.countplot(x='hours_per_week', data=df, order=['0-2 hours', '3-5 hours', '6-8 hours', '9-11 hours', '12+ hours'])
plt.title('Hours Per Week Spent Using AI Tools')
plt.xlabel('Hours per Week')
plt.ylabel('Count')
plt.savefig('plots/hours_per_week.png')

# 5. Benefit of AI tools for research activities
plt.figure(figsize=(10, 6))
sns.countplot(x='benefit', data=df)
plt.title('Benefit of AI Tools for Research Activities')
plt.xlabel('Benefit Rating')
plt.ylabel('Count')
plt.savefig('plots/benefit_rating.png')

# 6. Challenges faced with AI tools
plt.figure(figsize=(10, 6))
sns.countplot(x='challenging', data=df)
plt.title('Challenges Faced with AI Tools')
plt.xlabel('Challenge Rating')
plt.ylabel('Count')
plt.savefig('plots/challenges_rating.png')

# 7. Perceived grade improvement percentage
plt.figure(figsize=(10, 6))
sns.countplot(x='grade_improvement', data=df, order=['0-10%', '11-20%', '21-30%', '31-40%', '41+%'])
plt.title('Perceived Grade Improvement Since Using AI Tools')
plt.xlabel('Grade Improvement Percentage')
plt.ylabel('Count')
plt.savefig('plots/grade_improvement.png')

print("Visualizations have been saved in the 'plots' folder.")
