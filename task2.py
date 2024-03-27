import pandas as pd
import matplotlib.pyplot as plt

MATCHES = ["data science", "data scientist", "data engineer"]
RATING_VALUE = 4
AMOUNT_OF_TOP_STATES = 5
OTER_TRESHOLD = 2.5


# Load the CSV file into a DataFrame
jobs_df = pd.read_csv("Uncleaned_DS_jobs.csv")

########################## Pre-processing Data ##########################################################

#"""
# Unic job titles and counts
unique_job_titles = jobs_df["Job Title"].unique().tolist()
position_counts = jobs_df["Job Title"].value_counts()

# Combine the two lists using zip and convert to DataFrame and save it to CSV file
df = pd.DataFrame(list(zip(unique_job_titles, position_counts)), columns=['Job Title', 'Count'])
df.to_csv('job_title_counts.csv', index=False)

# Filter out job titles containing "data science" or "data scientist"
data_science_jobs = jobs_df[jobs_df["Job Title"].apply(lambda x: any(match in x.lower() for match in MATCHES))]

# Repersenting the rest of the data frame and counting uniques and the amount of entries
rest_of_table = jobs_df[~jobs_df["Job Title"].str.contains("data science|data scientist|data engineer", case=False)]
a = rest_of_table["Job Title"].value_counts()

#print(a)
#"""
#########################################################################################################

########################## Task_1 #######################################################################
"""
# Count the number of jobs per state
data_science_jobs_by_state= data_science_jobs["Location"].str.split(", ").str[-1]
jobs_per_state = data_science_jobs_by_state.value_counts()

# Get the top 5 states
top_states = jobs_per_state.head(AMOUNT_OF_TOP_STATES)

#print("Top 5 States with the Most Data Science Jobs:")
#print(top_states)
#print("Companies with a rating of 4.9 and above:")
#print(high_rating_company_list)
"""
############# Bar-type plot ################
"""
plt.figure(figsize = (10, 6))
top_states.plot(kind = "bar", color = "skyblue")
plt.title(" Top 5 States with the Most Data Science Jobs")
plt.xlabel("State")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
"""
############# Pie-type plot ################
"""
plt.figure(figsize=(10, 6))
top_states.plot(kind="pie", autopct='%1.1f%%', startangle=180)
plt.title("Top 5 States with the Most Data Science Jobs")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()
"""
############# Plot two plots at one fugure ################
"""
 #Plot two plots at one fugure

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
#########################################################################################################

########################## Task_2 #######################################################################

"""
# Filter out Company's names containing rating RATING_VALUE and above
data_science_jobs.loc[:, "Rating"] = pd.to_numeric(jobs_df["Rating"], errors="coerce")
high_rating_companies = jobs_df[jobs_df["Rating"] >= RATING_VALUE]
high_rating_company_list = high_rating_companies["Company Name"].tolist()

# Sorting high rating companies by rating
sorted_high_rating_companies = high_rating_companies.sort_values(by="Rating", ascending=False)

# Calculate the count of companies for each rating value
rating_counts = sorted_high_rating_companies["Rating"].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Companies by Rating')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

"""
#########################################################################################################

########################## Task_3 #######################################################################

"""

# Replace "-1" or NaN values in "Sector" with "No Data" in the copied DataFrame using .loc accessor
data_science_jobs.loc[data_science_jobs["Sector"].isna(), "Sector"] = "No Data"
data_science_jobs.loc[data_science_jobs["Sector"] == "-1", "Sector"] = "No Data"

# Calculate percentage of jobs in each sector
sector_percentage = (data_science_jobs["Sector"].value_counts() / len(data_science_jobs)) * 100

# Identify sectors with less than a treshold representation and group them under "Other"
sector_percentage["Other"] = sector_percentage[sector_percentage < OTER_TRESHOLD].sum()
sector_percentage = sector_percentage[sector_percentage >= OTER_TRESHOLD]

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sector_percentage, labels=sector_percentage.index, autopct='%1.1f%%', startangle=180,)
plt.title('Percentage of Data Science Jobs in Each Sector')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
"""
