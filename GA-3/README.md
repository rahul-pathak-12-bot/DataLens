# Dataset Documentation

## Overview
This repository contains a dataset related to gear assembly production, cost analysis, shift operations, and scrap data. The dataset is stored in an Excel file named `dataset_3_467.xlsx` and includes various details about production output, sales, and operational efficiency.

## File Details
- **Filename**: `dataset_3_467.xlsx`
- **Sheets**:
  1. **Data** – Contains production and sales details of gear assemblies.
  2. **Cost** – Provides cost breakdown including direct materials, labor, and overhead costs.
  3. **Shift_Running** – Logs operational status of shifts.
  4. **Actual_Output** – Records the actual production output per shift.
  5. **Scrap** – Tracks defective or waste production per shift.

## Data Dictionary
### 1. Data
| Column | Description |
|---------|------------|
| Gear Assembly | Type of gear assembly produced |
| GA Category | Category classification (e.g., BS4, BS6) |
| Month | Production month |
| Quarter | Fiscal quarter |
| Fiscal Year | Financial year of production |
| Quantity Produced | Total units produced |
| Sales Quantity | Number of units sold |
| Price | Selling price per unit |

### 2. Cost
| Column | Description |
|---------|------------|
| SALES DETAILS (GEAR ASSEMBLIES) | Name of the gear assembly |
| FY | Financial year |
| CC | Cost center (if available) |
| Direct Materials | Cost of raw materials per unit |
| Direct Labour | Labor cost per unit |
| Production Overhead | Overhead costs related to production |
| G&A Overhead | General & administrative expenses |
| Finance Costs | Financial costs associated with production |

### 3. Shift_Running
| Column | Description |
|---------|------------|
| Date | Date of operation |
| Shift 1 (8 Hours) | Status of Shift 1 (e.g., Operational, Maintenance) |
| Shift 2 (8 Hours) | Status of Shift 2 |
| Shift 3 (8 Hours) | Status of Shift 3 |

### 4. Actual_Output
| Column | Description |
|---------|------------|
| Date | Date of production |
| Shift 1 | Output quantity for Shift 1 |
| Shift 2 | Output quantity for Shift 2 |
| Shift 3 | Output quantity for Shift 3 |

### 5. Scrap
| Column | Description |
|---------|------------|
| Date | Date of production |
| Shift 1 | Scrap units recorded in Shift 1 |
| Shift 2 | Scrap units recorded in Shift 2 |
| Shift 3 | Scrap units recorded in Shift 3 |

## Use Case
This dataset is useful for:
- Production analysis and efficiency tracking.
- Cost management and financial planning.
- Evaluating operational uptime and downtime.
- Monitoring defective unit trends.

## License
This dataset is provided for analytical and educational purposes. Please cite this repository if used in any reports or projects.

## Contact
For any questions or clarifications, feel free to raise an issue or contribute to the repository.

