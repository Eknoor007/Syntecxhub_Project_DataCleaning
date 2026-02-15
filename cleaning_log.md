Data Cleaning Summary:

Cabin Column:
The Cabin column contained 327 missing values out of 418 (~78%). Due to high sparsity and limited analytical value, the column was removed to prevent noise in downstream analysis.

Age Column:
The Age column had 86 missing values. These were imputed using the median age to preserve dataset size while ensuring robustness against skewed distributions and outliers.

Fare Column:
The Fare column had 1 missing value. This value was filled using the median fare to maintain consistency with the imputation strategy used for other numerical variables.

Duplicates:
The dataset was checked for duplicate rows, and no duplicates were found.

Column Standardization:
All column names were converted to lowercase to ensure consistency and improve readability.