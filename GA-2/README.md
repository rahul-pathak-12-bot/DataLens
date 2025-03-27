# Dataset Documentation

## Overview
This repository contains a dataset related to SKU inventory management, sales, and stock transfers across multiple distribution centers (DCs). The dataset is stored in an Excel file named `dataset_2_162.xlsx` and includes information about SKU categories, sales transactions, opening stock, and stock transfers.

## File Details
- **Filename**: `dataset_2_162.xlsx`
- **Sheets**:
  1. **SKU MASTER** – Contains SKU details including description, category, and price.
  2. **Sales** – Records daily sales transactions by SKU, date, and city.
  3. **Opening Stock** – Provides the initial stock levels for SKUs across different cities.
  4. **STOCK TRANSFER** – Logs stock movements between locations over time.

## Data Dictionary
### 1. SKU MASTER
| Column | Description |
|---------|------------|
| SKU | Unique identifier for each product |
| Description | Name or brand of the SKU |
| Category | Product category (e.g., Fashion, Household, etc.) |
| Price | Selling price of the SKU |

### 2. Sales
| Column | Description |
|---------|------------|
| Date | Date of sale (YYYY-MM-DD) |
| SKU | Unique identifier of the sold product |
| Product Name | Name of the product |
| City | Location where the sale occurred |
| Sales | Number of units sold |

### 3. Opening Stock
| Column | Description |
|---------|------------|
| SKU | Unique identifier for each product |
| Description | Name of the SKU |
| Category | Product category |
| Mumbai, Pune, Aurangabad, Nashik | Initial stock quantity at respective locations |

### 4. STOCK TRANSFER
| Column | Description |
|---------|------------|
| SKU | Unique identifier for each product |
| Dates (Columns) | Daily stock transfer quantities to different cities |

## Use Case
This dataset is useful for inventory analysis, sales trend tracking, and distribution planning. Users can:
- Analyze stock levels at different DCs.
- Track SKU sales trends over time.
- Evaluate stock transfer patterns between cities.

## License
This dataset is provided for educational and analytical purposes. Please cite the repository if used in any reports or projects.

## Contact
For any questions or clarifications, feel free to raise an issue or contribute to the repository.