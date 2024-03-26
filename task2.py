import pandas as pd

# Load the CSV file into a DataFrame
jobs_df = pd.read_csv("Uncleaned_DS_jobs.csv")

# Filter out job titles containing 'data science' or 'data scientist'
data_science_jobs = jobs_df[jobs_df['Job Title'].str.contains('data science|data scientist', case=False)]

# Count the number of jobs per state
jobs_per_state = data_science_jobs['Location'].value_counts()

# Get the top 5 states
top_5_states = jobs_per_state.head(5)

print("Top 5 States with the Most Data Science Jobs:")
print(top_5_states)
