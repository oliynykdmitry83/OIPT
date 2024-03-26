import pandas as pd
import matplotlib.pyplot as plt


RATING_VALUE = 4
AMOUNT_OF_TOP_STATES = 5

# Load the CSV file into a DataFrame
jobs_df = pd.read_csv("Uncleaned_DS_jobs.csv")

# Filter out job titles containing "data science" or "data scientist"
data_science_jobs = jobs_df[jobs_df["Job Title"].str.contains("data science|data scientist", case=False)]

# Filter out Company's names containing reting 4.8 and above
jobs_df["Rating"] = pd.to_numeric(jobs_df["Rating"], errors="coerce")
high_rating_companies = jobs_df[jobs_df["Rating"] >= RATING_VALUE]
high_rating_company_list = high_rating_companies["Company Name"].tolist()

# Sorting high rating companies by rating
sorted_high_rating_companies = high_rating_companies.sort_values(by="Rating", ascending=False)

# Count the number of jobs per state
jobs_per_state = data_science_jobs["Location"].value_counts()

# Get the top 5 states
top_5_states = jobs_per_state.head(AMOUNT_OF_TOP_STATES)



#print("Top 5 States with the Most Data Science Jobs:")
#print(top_5_states)
#print("Companies with a rating of 4.9 and above:")
#print(high_rating_company_list)


"""
# Plot of two separate figures

plt.figure(figsize = (10, 6))
top_5_states.plot(kind = "bar", color = "skyblue")
plt.title(" Top 5 States with the Most Data Science Jobs")
plt.xlabel("State")
plt.ylabel("NUmber of Jobs")
plt.xticks(rotation=45)

plt.figure(figsize=(30, 8))
plt.bar(sorted_high_rating_companies["Company Name"], sorted_high_rating_companies["Rating"], color='skyblue',edgecolor="red")
plt.xlabel('Company Name')
plt.ylabel('Rating')
plt.title('Ratings of High-Rating Companies')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability

plt.tight_layout()
plt.show()
"""

""" Plot two plots at one fugure

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 12))

# Plot bar chart for top 5 states with the most data science jobs
top_5_states.plot(kind="bar", ax=axes[0], color="skyblue")
axes[0].set_title("Top 5 States with the Most Data Science Jobs")
axes[0].set_xlabel("State")
axes[0].set_ylabel("Number of Jobs")
axes[0].tick_params(axis='x', rotation=45)

# Plot bar chart for ratings of high-rating companies
high_rating_companies.plot(kind="bar", x="Company Name", y="Rating", ax=axes[1], color="skyblue", edgecolor="red")
axes[1].set_title("Ratings of High-Rating Companies")
axes[1].set_xlabel("Company Name")
axes[1].set_ylabel("Rating")
axes[1].tick_params(axis='x', rotation=90)

plt.tight_layout()
plt.show()

"""

# Calculate the count of companies for each rating value
rating_counts = sorted_high_rating_companies["Rating"].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Companies by Rating')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
