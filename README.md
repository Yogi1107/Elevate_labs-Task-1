# Data Cleaning and Preparation Script

This repository contains a Python script that performs essential data cleaning operations on a raw dataset. It is designed to clean real-world CSV files containing missing values, duplicates, inconsistent formats, and incorrect data types — all common challenges in data preprocessing.

---

## Features

The script performs the following tasks:

-  Identify and handle missing values (fill or drop)
-  Remove duplicate rows
-  Standardize text fields (e.g., gender, country names)
-  Convert date formats to a consistent type (e.g., `dd-mm-yyyy`)
-  Rename column headers (e.g., lowercase, no spaces)
-  Check and correct data types (e.g., convert age to `int`, dates to `datetime`)

---

##  Input

- A raw `.csv` file (e.g., `Medical_appointment.csv`) with common issues such as:
  - Null or missing entries
  - Duplicate records
  - Mixed case or inconsistent text formats
  - Date columns in ISO or string format
  - Misnamed or improperly formatted column headers

---

##  How to Use

###  Prerequisites

Make sure you have **Python 3** and **pandas** installed:

```bash
pip install pandas
```

### Running the Script
Place your input CSV file (e.g., Medical_appointment.csv) in the same directory.

Run the script:

```bash
python clean_data.py
```

The cleaned dataset will be saved as:
```bash
cleaned_medical_appointment.csv
```
