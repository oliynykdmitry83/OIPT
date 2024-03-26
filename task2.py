import pandas as pd
import matplotlib.pyplot as plt


rating_value = 4.9
amount_of_top_states = 5

# Load the CSV file into a DataFrame
jobs_df = pd.read_csv("Uncleaned_DS_jobs.csv")

# Filter out job titles containing "data science" or "data scientist"
data_science_jobs = jobs_df[jobs_df["Job Title"].str.contains("data science|data scientist", case=False)]

# Filter out Company's names containing reting 4.9 and above
jobs_df["Rating"] = pd.to_numeric(jobs_df["Rating"], errors="coerce")
high_rating_companies = jobs_df[jobs_df["Rating"] >= rating_value]
high_rating_company_list = high_rating_companies["Company Name"].tolist()

# Count the number of jobs per state
jobs_per_state = data_science_jobs["Location"].value_counts()

# Get the top 5 states
top_5_states = jobs_per_state.head(amount_of_top_states)



print("Top 5 States with the Most Data Science Jobs:")
print(top_5_states)
print("Companies with a rating of 4.9 and above:")
print(high_rating_company_list)

"""
plt.figure(figsize = (10, 6))
top_5_states.plot(kind = "bar", color = "skyblue")
plt.title(" Top 5 States with the Most Data Science Jobs")
plt.xlabel("State")
plt.ylabel("NUmber of Jobs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""
