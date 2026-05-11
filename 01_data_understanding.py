import pandas as pd
import numpy as np
df = pd.read_csv("/Users/kshiva/Documents/ScreenSense_Project/data/raw/Indian_Kids_Screen_Time.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())

# Age Band
#bins = [5, 9, 12, 15, 18]
#labels = ["6-9", "10-12", "13-15", "16-18"]
#df["Age_Band"] = pd.cut(df["Age"], bins=bins, labels=labels)

# Screen Time Level
#df["Screen_Time_Level"] = pd.cut(
 #   df["Avg_Daily_Screen_Time_hr"],
  #  bins=[0, 2, 4, 6, 24],
   # labels=["Low", "Moderate", "High", "Very High"]
#)

# Usage Balance
#df["Usage_Balance"] = np.where(
 #   df["Educational_to_Recreational_Ratio"] > 1,
  #  "More Educational",
   # "More Recreational"
#)
#print(df["Age_Band"].value_counts())
#print(df["Screen_Time_Level"].value_counts())
#print(df["Usage_Balance"].value_counts())

#df.to_csv("/Users/kshiva/Documents/ScreenSense_Project/data/processed/screensense_clean.csv", index=False)



def feature_engineering(df):

    # Age Band
    bins = [5, 9, 12, 15, 18]
    labels = ["6-9", "10-12", "13-15", "16-18"]
    df["Age_Band"] = pd.cut(df["Age"], bins=bins, labels=labels)

    # Screen Time Level
    df["Screen_Time_Level"] = pd.cut(
        df["Avg_Daily_Screen_Time_hr"],
        bins=[0, 2, 4, 6, 24],
        labels=["Low", "Moderate", "High", "Very High"]
    )

    # Usage Balance
    df["Usage_Balance"] = np.where(
        df["Educational_to_Recreational_Ratio"] > 1,
        "More Educational",
        "More Recreational"
    )

    return df

df = feature_engineering(df)

df.to_csv("/Users/kshiva/Documents/ScreenSense_Project/data/processed/screensense_clean.csv", index=False)