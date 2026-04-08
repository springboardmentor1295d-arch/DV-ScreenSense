import pandas as pd

df = pd.read_csv("Indian_Kids_Screen_Time.csv")

df.columns = [c.strip() for c in df.columns]

def age_band(age):
    if age <= 10:
        return "5-10"
    elif age <= 15:
        return "11-15"
    else:
        return "16-20"

df["Age_Band"] = df["Age"].apply(age_band)

def activity_category(ratio):
    if ratio >= 0.75:
        return "Mostly Educational"
    elif ratio >= 0.4:
        return "Balanced"
    else:
        return "Mostly Recreational"

df["Activity_Category"] = df["Educational_to_Recreational_Ratio"].apply(activity_category)

# Health risk flag
df["Health_Risk_Flag"] = df["Health_Impacts"].apply(
    lambda x: "No Risk" if pd.isna(x) or x == "No Issues" else "Risk"
)

df.to_csv("ScreenSense_Cleaned_Dataset.csv", index=False)