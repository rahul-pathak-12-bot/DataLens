# Dataset Documentation

## Overview
This repository contains a dataset related to consumer demographics, purchasing behavior, and loan details. The dataset is stored in an Excel file named `dataset_1_193.xlsx` and consists of two sheets: `Data_1` (consumer survey data) and `Data_2` (loan-related data).

## File Details
- **Filename**: `dataset_1_193.xlsx`
- **Sheets**:
  1. **Data_1** – Contains survey-based consumer data.
  2. **Data_2** – Includes details on loan issuance and borrower profiles.

## Data Dictionary
### 1. Data_1 (Consumer Survey Data)
| Column | Description |
|---------|------------|
| STATE | State where the consumer resides |
| REGION_TYPE | Urban or rural classification |
| RESPONSE_STATUS | Survey response status (e.g., Accepted, Non-Response) |
| AGE_GROUP | Age category of the consumer |
| INCOME_GROUP | Annual income range |
| OCCUPATION_GROUP | Consumer's occupation category |
| EDUCATION_GROUP | Educational background classification |
| GENDER_GROUP | Gender distribution (Balanced, Male Majority, etc.) |
| POWER_GROUP | Access to electricity (e.g., 12-24 hours, 24 hours) |
| TRAVEL_GROUP | Average daily travel time |
| WILL_BUY_TWO_WHEELER_NOW | Indicates if the consumer is currently interested in purchasing a two-wheeler (Y/N) |
| GOOD_TIME_TO_BUY_TWO_WHEELER | Suggested timeframe for purchasing a two-wheeler |
| HAS_OUTSTANDING_SAVING_IN_FIXED_DEPOSITS | Whether the consumer has fixed deposit savings (Y/N) |
| HAS_OUTSTANDING_BORROWING | Whether the consumer has any outstanding borrowings (Y/N) |
| BORROWED_FOR_CONSUMPTION_EXPENDITURE | Indicates if the consumer borrowed for general expenses (Y/N) |
| BORROWED_FOR_CONSUMER_DURABLES | Indicates if the consumer borrowed for durable goods (Y/N) |
| BORROWED_FOR_VEHICLES | Indicates if the consumer borrowed to buy a vehicle (Y/N) |
| BORROWED_FROM_BANK | Indicates if the consumer borrowed from a bank (Y/N) |
| BORROWED_FROM_BANK_FOR_VEHICLES | Indicates if the bank loan was used for a vehicle purchase (Y/N) |

### 2. Data_2 (Loan Information)
| Column | Description |
|---------|------------|
| Loan Id | Unique loan identifier |
| Quarters | Quarter in which the loan was issued |
| Years | Financial year of loan issuance |
| Segment of Loan | Type of loan segment (e.g., Commercial) |
| Lender Name | Lending institution name (e.g., NBFC) |
| Type of Loan | Loan category (e.g., Commercial Loan) |
| Original Loan size | Initial loan amount sanctioned |
| Outstanding loan amount | Remaining balance on the loan |
| Borrower Age | Age of the loan borrower |
| Borrower Income | Annual income of the borrower |
| New to Credit (Y/N) | Indicates if the borrower is new to credit |
| Gender | Gender of the borrower |

## Use Case
This dataset is useful for:
- Consumer behavior analysis and market segmentation.
- Loan issuance trends and credit risk assessment.
- Identifying demand for two-wheelers and financial borrowing patterns.

## License
This dataset is provided for analytical and research purposes. Please cite this repository if used in any reports or projects.

## Contact
For any questions or clarifications, feel free to raise an issue or contribute to the repository.

