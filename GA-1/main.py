import pandas as pd

# Load dataset
file_path = "dataset_1_193.xlsx"
df = pd.read_excel(file_path, sheet_name="Data_1", skiprows=1)

# 1. Fraction of households with only one two-wheeler
fraction_one_two_wheeler = (df['TWO_WHEELERS_OWNED'] == 1).mean()

# 2. Fraction of households with no two-wheeler but interested in buying one
fraction_no_tw_but_will_buy = ((df['TWO_WHEELERS_OWNED'] == 0) & (df['WILL_BUY_TWO_WHEELER'] == 'Y')).mean()

# 3. Proportion of households with a two-wheeler but interested in buying one more
fraction_have_tw_but_will_buy = ((df['TWO_WHEELERS_OWNED'] > 0) & (df['WILL_BUY_TWO_WHEELER'] == 'Y')).mean()

# 4. Fraction of urban households with no two-wheeler but intending to buy immediately
fraction_urban_no_tw_buy_now = ((df['REGION_TYPE'] == 'URBAN') & (df['TWO_WHEELERS_OWNED'] == 0) & (df['WILL_BUY_TWO_WHEELER_NOW'] == 'Y')).mean()

# 5. Existing market share of commuter bikes
market_share_commuter_bikes = (df['TYPE_OF_TWO_WHEELER_OWNED'] == 'Commuter Bike').mean()

# 6. Proportion of female-dominated households with a scooter
female_dominated = df['GENDER_GROUP'].isin(['Female Majority', 'Female Dominant', 'Only Female'])
fraction_female_scooter = (female_dominated & (df['TYPE_OF_TWO_WHEELER_OWNED'] == 'Scooter')).mean()

# 7. Proportion of households eligible for a new loan (no outstanding borrowing)
fraction_eligible_new_loan = (df['HAS_OUTSTANDING_BORROWING'] == 'N').mean()

# 8. Proportion of households wanting to buy a two-wheeler and eligible for a lower interest loan against FD
fraction_fd_secured_loan = ((df['WILL_BUY_TWO_WHEELER'] == 'Y') & (df['HAS_OUTSTANDING_SAVING_IN_FIXED_DEPOSITS'] == 'Y')).mean()

# 9. Target market share for electric two-wheelers (24-hour power availability & interested in buying)
fraction_electric_tw_market = ((df['WILL_BUY_TWO_WHEELER'] == 'Y') & (df['POWER_GROUP'] == '24 hours')).mean()

# 10. Fraction of rural farmers having at least one two-wheeler
fraction_rural_farmers_tw = ((df['REGION_TYPE'] == 'RURAL') & (df['OCCUPATION_GROUP'].str.contains('Farmer', na=False)) & (df['TWO_WHEELERS_OWNED'] > 0)).mean()

# Print results
results = {
    "Fraction of households with only one two-wheeler": fraction_one_two_wheeler,
    "Fraction of households with no two-wheeler but want to buy": fraction_no_tw_but_will_buy,
    "Proportion of households with a two-wheeler but want to buy one more": fraction_have_tw_but_will_buy,
    "Fraction of urban households with no two-wheeler but intending to buy immediately": fraction_urban_no_tw_buy_now,
    "Market share of commuter bikes": market_share_commuter_bikes,
    "Proportion of female-dominated households with a scooter": fraction_female_scooter,
    "Proportion of households eligible for a new loan": fraction_eligible_new_loan,
    "Proportion of households wanting to buy a two-wheeler and eligible for FD loan": fraction_fd_secured_loan,
    "Target market share for electric two-wheelers": fraction_electric_tw_market,
    "Fraction of rural farmers with at least one two-wheeler": fraction_rural_farmers_tw
}

for key, value in results.items():
    print(f"{key}: {value:.4f}")

# Fraction of households with only one two-wheeler: 0.4900
# Fraction of households with no two-wheeler but want to buy: 0.0400
# Proportion of households with a two-wheeler but want to buy one more: 0.0700
# Fraction of urban households with no two-wheeler but intending to buy immediately: 0.0200
# Market share of commuter bikes: 0.3100
# Proportion of female-dominated households with a scooter: 0.0300
# Proportion of households eligible for a new loan: 0.4900
# Proportion of households wanting to buy a two-wheeler and eligible for FD loan: 0.0700
# Target market share for electric two-wheelers: 0.0800
# Fraction of rural farmers with at least one two-wheeler: 0.0200