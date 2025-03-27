import pandas as pd
import numpy as np
from datetime import datetime
from google.colab import files
uploaded = files.upload()

file_name = list(uploaded.keys())[0]

raw = pd.read_excel(file_name)

# ---- 1. Renaming Columns ----
raw.rename(columns={"Year of experience": "Years of experience"}, inplace=True)

# ---- 2. YoE Score (AbsMax Normalization) ----
raw["YoE Score"] = raw["Years of experience"] / raw["Years of experience"].abs().max()

# ---- 3. Valid Appraisals ----
raw["Valid Appraisals"] = ((raw["Appraisal 1"] > 0.7).astype(int) +
                           (raw["Appraisal 2"] > 0.7).astype(int) +
                           (raw["Appraisal 3"] > 0.7).astype(int))

# ---- 4. Appraisal Score (AbsMax Normalization) ----
raw["Appraisal Score"] = raw["Valid Appraisals"] / raw["Valid Appraisals"].abs().max()

# ---- 5. No. of Skills ----
raw["No. of Skills"] = raw["Skills"].str.count(",") + 1

# ---- 6. Skill Score (Normalized) ----
raw["Skill Score"] = raw["No. of Skills"] / raw["No. of Skills"].max()

# ---- 7. No. of Projects ----
raw["No. of Projects"] = raw["Key projects"].str.count(",") + 1

# ---- 8. Project Score (Normalized) ----
raw["Project Score"] = raw["No. of Projects"] / raw["No. of Projects"].max()

# ---- 9. Experience Score (Normalized) ----
raw["Experience Score"] = raw["Duration in the current role"] / raw["Duration in the current role"].max()

# ---- 10. Bench Score (Normalized) ----
raw["Bench Score"] = raw["Bench duration"] / raw["Bench duration"].max()

# ---- 11. Days to Availability ----
today = datetime(2024, 7, 1)

# Convert to datetime, then to date only
raw["When the candidate will be available"] = pd.to_datetime(raw["When the candidate will be available"]).dt.date

# Corrected Days to Availability calculation
raw["Days to Availability"] = (raw["When the candidate will be available"] - today.date()).apply(lambda x: x.days)

# ---- 12. Availability Score (1 - Normalized Days) ----
raw["Availability Score"] = 1 - (raw["Days to Availability"] / raw["Days to Availability"].max())

# ---- 13. Today Column ----
raw["Today"] = today.date()

# ---- 14. Method 1 Score (Sum of all scores) ----
raw["Method 1 Score"] = raw[["YoE Score", "Appraisal Score", "Skill Score", "Project Score",
                             "Experience Score", "Bench Score", "Availability Score"]].sum(axis=1)

# ---- 15. Method 2 Score (Weighted Sum) ----
raw["Method 2 Score"] = (0.2 * raw["YoE Score"] +
                         0.1 * raw["Appraisal Score"] +
                         0.2 * raw["Skill Score"] +
                         0.1 * raw["Project Score"] +
                         0.1 * raw["Experience Score"] +
                         0.1 * raw["Bench Score"] +
                         0.2 * raw["Availability Score"])


# ---- 16. Method 1 Rank ----
raw["Method 1 Rank"] = raw["Method 1 Score"].rank(ascending=False, method='min').astype(int)

# ---- 17. Method 2 Rank ----
raw["Method 2 Rank"] = raw["Method 2 Score"].rank(ascending=False, method='min').astype(int)

output_file = "processed.xlsx"
raw.to_excel(output_file, index=False)

# Display only the specified columns
print(" Filtered Output Preview:")
print(raw[["Employee name", "Method 1 Score", "Method 2 Score", "Method 1 Rank", "Method 2 Rank"]])


# Question 1. Rank of Akanksha using Method 1 (integer)
rank_akanksha = raw.loc[raw["Employee name"] == "Akanksha", "Method 1 Rank"].values[0]

# Question 2. Composite score of Praveen using Method 1 (float) 
score_praveen = raw.loc[raw["Employee name"] == "Praveen", "Method 1 Score"].values[0]

# Question 3. Rank of Nanda using Method 2 (integer) 
rank_nanda = raw.loc[raw["Employee name"] == "Nanda", "Method 2 Rank"].values[0]

# Question 4. Composite score of Sazid using Method 2 (float) 
score_sazid = raw.loc[raw["Employee name"] == "Sazid", "Method 2 Score"].values[0]

# Question 5. Count of persons with the same rank in both methods 
same_rank_count = (raw["Method 1 Rank"] == raw["Method 2 Rank"]).sum()

print("\n Results:")
print(f"1 Rank of Akanksha using Method 1: {int(rank_akanksha)}")
print(f"2 Composite score of Praveen using Method 1: {score_praveen:.4f}")
print(f"3 Rank of Nanda using Method 2: {int(rank_nanda)}")
print(f"4 Composite score of Sazid using Method 2: {score_sazid:.4f}")
print(f"5 Number of persons with the same rank in both methods: {same_rank_count}")