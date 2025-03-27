import pandas as pd
from google.colab import files
import os
uploaded = files.upload()
filename = list(uploaded.keys())[0]

data = pd.read_excel(filename, sheet_name="Data")
cost = pd.read_excel(filename, sheet_name="Cost")
shift_running = pd.read_excel(filename, sheet_name="Shift_Running")
actual_output = pd.read_excel(filename, sheet_name="Actual_Output")
scrap = pd.read_excel(filename, sheet_name="Scrap")

# Question 1:Which BS4 only Gear Assembly saw the maximum sales in the first quarter of any given year?
data[(data["GA Category"]=="BS4 Only") & (data["Quarter"]=="Q1")].sort_values(by="Sales Quantity", ascending=False)["Gear Assembly"].values[0]
# Answer: "Gear Assembly 2 (BS4)"


# Question 2:Based on the data, which is Gear Assembly is incurring maximum (net) loss?
cost["Total Cost"] = (cost["Direct Materials"] + cost["Direct Labour"] + cost["Production Overhead"] + cost["G&A Overhead"] + cost["Finance Costs"])
cost.rename(columns={'SALES DETAILS (GEAR ASSEMBLIES)': 'Gear Assembly', 'FY': 'Fiscal Year'}, inplace=True)
merged_df = data.merge(cost, left_on=["Gear Assembly", "Fiscal Year"], right_on=["Gear Assembly", "Fiscal Year"], how='left')
merged_df["Total Cost"] = merged_df["Total Cost"] * merged_df["Sales Quantity"]
merged_df["Total Revenue"] = merged_df["Sales Quantity"] * merged_df["Price"]
merged_df["Net Loss"] = merged_df["Total Cost"] - merged_df["Total Revenue"]
gear_assembly_with_maximum_incurring_net_loss = merged_df.loc[merged_df["Net Loss"].idxmax(), "Gear Assembly"]
gear_assembly_with_maximum_incurring_net_loss
# Answer: "Gear Assembly 6 (BS6))"


# Question 3:Which Gear Assembly returned the highest percentage unit (net) margin?
# Unit Cost = Total Cost/Sales Quantity
# Unit Revenue = Total Revenue / Sales Quantity
# Net Margin=(Unit Revenue−Unit CostUnit Revenue)×100
merged_df["Unit Cost"] = merged_df["Total Cost"] / merged_df["Sales Quantity"]
merged_df["Unit Revenue"] = merged_df["Total Revenue"]/ merged_df['Sales Quantity']
merged_df["Net Margin"] = ((merged_df["Unit Revenue"] - merged_df["Unit Cost"])/merged_df["Unit Revenue"])*100
gear_assembly_with_highest_percentage_unit_margin = merged_df[merged_df["Net Margin"]==merged_df["Net Margin"].max()]["Gear Assembly"].values[0]
gear_assembly_with_highest_percentage_unit_margin
# Answer:"Gear Assembly 5 (BS6)"


# Question 4: Which period saw the least amount of ending inventory in terms of volume?
data["Period"] = data["Quarter"].astype(str) + " " + data["Fiscal Year"].astype(str)
# Calculate Ending Inventory (Unsold units)
data["Ending Inventory"] = data["Quantity Produced"] - data["Sales Quantity"]
data["Ending Inventory"] = data["Ending Inventory"].clip(lower=0)  
# Find the period with the least total ending inventory
period_inventory = data.groupby("Period")["Ending Inventory"].sum()
least_inventory_period = period_inventory.idxmin()
least_inventory_value = period_inventory.min()
# Print results
print("Period with the least ending inventory:", least_inventory_period)
print("Least ending inventory value:", least_inventory_value)
# Answer: "Period with the least ending inventory: Q2 2021-22
# Least ending inventory value: 5260"


# Question 5: Which Gear Assembly made the maximum jump in the percentage revenue from 2019-20 to 2020-21?
data["Total Revenue"] = data["Sales Quantity"] * data["Price"]
# Group by Gear Assembly and Fiscal Year, then sum Total Revenue
revenue_by_year = data.groupby(["Gear Assembly", "Fiscal Year"])["Total Revenue"].sum().unstack()
# Calculate percentage change from 2019-20 to 2020-21
revenue_by_year["Percentage Change"] = (
    (revenue_by_year["2020-21"] - revenue_by_year["2019-20"]) /
    revenue_by_year["2019-20"]
) * 100
# Find the Gear Assembly with the maximum percentage increase
max_jump = revenue_by_year["Percentage Change"].idxmax()
max_value = revenue_by_year["Percentage Change"].max()
print(f"Gear Assembly with maximum revenue jump: {max_jump} ")
# Answer: "Gear Assembly with maximum revenue jump: Gear Assembly 2 (BS4)"


# Question 6:What is the Overall Equipment Effectiveness (OEE) of manufacturing in Week-1(01-04-2022 to 07-04-2022 both days included)? (FLOAT BETWEEN 0 AND 1)
# Formula: OEE = Availability × Performance × Quality
# Convert dates to datetime format
shift_running["Date"] = pd.to_datetime(shift_running["Date"])
actual_output["Date"] = pd.to_datetime(actual_output["Date"])
scrap["Date"] = pd.to_datetime(scrap["Date"])
# Filter for Week-1 (01-07 April 2022)
week_filter = (actual_output["Date"] >= "2022-04-01") & (actual_output["Date"] <= "2022-04-07")
week_1_output = actual_output[week_filter]
week_1_scrap = scrap[week_filter]
# 1. Availability Calculation (FIXED)
# Count all non-operational shifts (Breakdown/Unplanned Maintenance/Power Cut)
shift_status_week1 = shift_running[week_filter].iloc[:, 1:]
availability = (
    shift_status_week1.isin(["Operational"]).sum().sum() /
    (3 * 7)  # 3 shifts/day × 7 days
)
# 2. Performance Calculation (FIXED)
rated_per_shift = 4000  # As per problem statement
actual_total = week_1_output.iloc[:, 1:].sum().sum()
expected_output = rated_per_shift * (shift_status_week1 == "Operational").sum().sum()
performance = min(actual_total / expected_output, 1.0)
# 3. Quality Calculation
total_scrap = week_1_scrap.iloc[:, 1:].sum().sum()
quality = (actual_total - total_scrap) / actual_total
# Compute OEE
oee = availability * performance * quality
print(round(oee, 3))
# Answer: "0.853"


#Question 7: What is the overall quality of the manufacturing process during the fortnight? (FLOAT BETWEEN 0 AND 1)
# Quality = Good Units/Total Unit Produced`
# Filter data for the fortnight (01-Apr-2022 to 14-Apr-2022)
fortnight_output = actual_output[(actual_output["Date"] >= "2022-04-01") &
                                 (actual_output["Date"] <= "2022-04-14")]
fortnight_scrap = scrap[(scrap["Date"] >= "2022-04-01") &
                        (scrap["Date"] <= "2022-04-14")]
# Compute total actual output and scrap for the fortnight
total_actual_output_fortnight = fortnight_output.iloc[:, 1:].sum().sum()  # Sum all shift values
total_scrap_fortnight = fortnight_scrap.iloc[:, 1:].sum().sum()  # Sum all scrap values
# Compute quality
quality_fortnight = (total_actual_output_fortnight - total_scrap_fortnight) / total_actual_output_fortnight
# Ensure quality is between 0 and 1
quality_fortnight = min(max(quality_fortnight, 0), 1)
# Display the result
quality_fortnight
# Answer: "np.float64(0.9949845295594734)"


# Question 8:What is the performance of the manufacturing process during Week-2? (FLOAT BETWEEN 0 AND 1)
week_2_dates = (actual_output["Date"] >= "2022-04-08") & (actual_output["Date"] <= "2022-04-14")
week_2_output = actual_output[week_2_dates]
# Get operational shifts from Shift_Running data
week_2_shifts = shift_running[shift_running["Date"].isin(week_2_output["Date"])]
operational_shifts = (week_2_shifts.iloc[:, 1:] == "Operational").sum().sum()
# Compute theoretical maximum based on ACTUAL OPERATIONAL SHIFTS (not total planned)
rated_output_per_shift = 4000  # As per problem statement
theoretical_max_output_week_2 = operational_shifts * rated_output_per_shift
# Compute actual output
total_actual_output_week_2 = week_2_output.iloc[:, 1:].sum().sum()
# Compute performance (capped at 100%)
performance_week_2 = min(total_actual_output_week_2 / theoretical_max_output_week_2, 1.0)
print(f"Week-2 Performance: {performance_week_2:.3f}")
# Answer: "Week-2 Performance: 1.000"


# Question 9:What is the average number of parts manufactured per hour during the fortnight? Assume that a shift runs for 8 hours and there is no break between shifts. (INTEGER) (Round down the answer to the nearest whole number. 
# E.g. We can’t have 2.3 parts, so the answer will be 2 parts)
# Parts per hour= Total Hours Worked/Total Actual Output`
# Calculate total operational hours during the fortnight
# First, count operational shifts from Shift_Running data
operational_shifts = (shift_running.iloc[:, 1:] == "Operational").sum().sum()
# Total operational hours (exclude non-production time)
total_hours_fortnight = operational_shifts * 8  
# Sum actual output for the fortnight (01-14 April)
total_actual_output_fortnight = actual_output.iloc[:, 1:].sum().sum() 
# Compute parts/hour (rounded down)
parts_per_hour = total_actual_output_fortnight // total_hours_fortnight  
print(f"Average parts/hour: {parts_per_hour}")  
# Answer: "Average parts/hour: 524"


# Question 10: The company uses MAPE (Mean Absolute Percentage Error) to measure process variability in the manufacturing process. 
# Which shift sees the maximum process variability during the fortnight? E.g. Shift 1 (STRING)`
def get_mape(shift_series, rated_output_shift):
    shfit_series_new = shift_series[shift_series != 0]
    n = shfit_series_new.shape[0]

    abs_value = ((shfit_series_new - rated_output_shift) / shfit_series_new).abs().sum()

    mape = (1 / n) * abs_value * 100
    return mape
mape = dict()
for col in actual_output.columns.to_list()[1:]:
    mape[get_mape(actual_output[col], rated_output_per_shift)] = col

a = mape[max(mape.keys())]
a
# Answer: "Shift 3"