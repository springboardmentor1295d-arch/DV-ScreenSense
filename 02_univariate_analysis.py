import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("/Users/kshiva/Documents/ScreenSense_Project/data/processed/screensense_clean.csv")

# Histogram
plt.figure()
plt.hist(df["Avg_Daily_Screen_Time_hr"], bins=20)
plt.title("Distribution of Average Daily Screen Time")
plt.xlabel("Average Daily Screen Time (Hours)")
plt.ylabel("Number of Kids")
plt.show()
#1. Distribution of Average Daily Screen Time
#The histogram shows that most children spend between 3 to 5 hours per day on screens.
#The distribution appears slightly right-skewed, indicating a smaller group of children with very high screen time (above 6 hours).
#This suggests that while moderate usage is common, a noticeable portion of children may be at risk of excessive screen exposure.




plt.figure()
df["Age_Band"].value_counts().plot(kind="bar")
plt.title("Age Band Distribution")
plt.xlabel("Age Band")
plt.ylabel("Number of Kids")
plt.show()
#2. Age Band Distribution
#The 13–15 age group represents the largest segment in the dataset, followed closely by 16–18 and 10–12.
#The 6–9 age group has the smallest representation.
#This suggests that early and mid-teen children dominate the sample, which may influence overall screen time trends.


plt.figure()
df["Primary_Device"].value_counts().plot(kind="bar")
plt.title("Primary Device Used by Kids")
plt.xlabel("Device Type")
plt.ylabel("Number of Kids")
plt.show()
#3. Primary Device Usage
#Smartphones are the most commonly used device among children, with over 4,000 users.
#This suggests that mobile accessibility plays a major role in screen exposure.
#Other devices like tablets and laptops are comparatively less dominant.


plt.figure()
df.groupby("Age_Band")["Avg_Daily_Screen_Time_hr"].mean().plot(kind="bar")
plt.title("Average Screen Time by Age Band")
plt.xlabel("Age Band")
plt.ylabel("Average Daily Screen Time (Hours)")
plt.show()
#4. Age Band vs Screen Time
#The 16–18 age group has the highest average daily screen time among all age bands.
#Screen time increases progressively with age, indicating that older teens are more exposed to digital devices.
#This trend suggests greater independence and device ownership in older cohorts.

plt.figure()
df.groupby("Gender")["Avg_Daily_Screen_Time_hr"].mean().plot(kind="bar")
plt.title("Average Screen Time by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Daily Screen Time (Hours)")
plt.show()
#5. Gender vs Screen Time
#Male students have slightly higher average screen time compared to females, although the difference is minimal.
#This indicates that screen usage patterns are relatively similar across genders, with no major disparity in exposure levels.

plt.figure()
df.groupby("Urban_or_Rural")["Avg_Daily_Screen_Time_hr"].mean().plot(kind="bar")
plt.title("Average Screen Time by Location Type")
plt.xlabel("Location Type")
plt.ylabel("Average Daily Screen Time (Hours)")
plt.show()
#6. Urban vs Rural Screen Time
#Rural children show slightly higher average daily screen time compared to urban children.
#This may suggest increasing digital penetration in rural areas or limited alternative recreational activities.
#The difference, however, is not extremely large.

high_risk = df[df["Screen_Time_Level"].isin(["High", "Very High"])]

plt.figure()
high_risk["Primary_Device"].value_counts().plot(kind="bar")
plt.title("Primary Device Among High Screen Time Users")
plt.xlabel("Device Type")
plt.ylabel("Number of High-Risk Kids")
plt.show()
#7. Device Share Among High-Risk Users
#Smartphones are the most dominant device among high screen time users.
#This indicates that excessive screen exposure is strongly associated with mobile phone usage.
#Policy interventions or parental monitoring strategies may need to focus primarily on smartphone usage.
