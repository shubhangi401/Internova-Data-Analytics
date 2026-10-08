import numpy as np
import pandas as pd
# Create NumPy array containing at least 10 numbers
# numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# print("NumPy Array:")
# print(numbers)

# # Display shape
# print("Shape:", numbers.shape)

# # Display size
# print("Size:", numbers.size)

# # Display data type
# print("Data Type:", numbers.dtype)

# # One-dimensional array
# one_d = np.array([1, 2, 3, 4, 5, 6])

# print("\nOne-Dimensional Array:")
# print(one_d)

# # Two-dimensional array
# two_d = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# print("\nTwo-Dimensional Array:")
# print(two_d)

# print("2D Array Shape:", two_d.shape)

# TASK 2: NumPy Indexing, Slicing & Reshaping
# ============================================================

# print("\n========== TASK 2: Indexing, Slicing & Reshaping ==========")

# arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# # Indexing
# print("First element:", arr[0])
# print("Fifth element:", arr[4])
# print("Last element:", arr[-1])

# # Slicing
# print("\nFirst five elements:")
# print(arr[:5])

# print("Elements from index 2 to 6:")
# print(arr[2:7])

# print("Last three elements:")
# print(arr[-3:])

# # Create 2D array
# matrix = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# print("\n2D Array:")
# print(matrix)

# # Access rows
# print("\nFirst Row:")
# print(matrix[0])

# print("Second Row:")
# print(matrix[1])

# # Access columns
# print("First Column:")
# print(matrix[:, 0])

# print("Second Column:")
# print(matrix[:, 1])

# # Access specific element
# print("Element at row 2, column 3:")
# print(matrix[1, 2])

# # Reshaping
# original = np.array([
#     1, 2, 3, 4,
#     5, 6, 7, 8,
#     9, 10, 11, 12
# ])

# reshaped = original.reshape(3, 4)

# print("\nOriginal Array:")
# print(original)

# print("\nReshaped Array:")
# print(reshaped)
# TASK 3: NumPy Mathematical & Statistical Operations
# ============================================================

# print("\n========== TASK 3: Mathematical & Statistical Operations ==========")

# a = np.array([10, 20, 30, 40, 50])
# b = np.array([5, 10, 15, 20, 25])

# print("Array A:", a)
# print("Array B:", b)

# # Mathematical operations
# print("\nAddition:")
# print(a + b)

# print("\nSubtraction:")
# print(a - b)

# print("\nMultiplication:")
# print(a * b)

# print("\nDivision:")
# print(a / b)

# # Statistical dataset
# dataset = np.array([10, 20, 30, 40, 50, 60, 70])

# print("\nStatistical Operations:")

# print("Mean:", np.mean(dataset))

# print("Median:", np.median(dataset))

# print("Minimum:", np.min(dataset))

# print("Maximum:", np.max(dataset))

# print("Standard Deviation:", np.std(dataset))

# print("Sum:", np.sum(dataset))
# TASK 4: Pandas Series & DataFrame
# ============================================================

# print("\n========== TASK 4: Pandas Series & DataFrame ==========")

# Create Pandas Series
# marks_series = pd.Series(
#     [85, 78, 92, 88, 76],
#     index=["Amit", "Sneha", "Rahul", "Priya", "Neha"]
# )

# print("Pandas Series:")
# print(marks_series)

# #Create DataFrame
# students = pd.DataFrame({
#     "Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
#     "Age": [20, 21, 20, 22, 21],
#     "Marks": [85, 78, 92, 88, 76],
#     "Department": [
#         "CSE",
#         "Data Science",
#         "CSE",
#         "Data Science",
#         "CSE"
#     ]
# })

# print("\nStudent DataFrame:")
# print(students)

# # Column names
# print("\nColumn Names:")
# print(students.columns)

# # Index
# print("\nIndex:")
# print(students.index)

# # Add new column
# students["Result"] = np.where(
#     students["Marks"] >= 40,
#     "Pass",
#     "Fail"
# )

# print("\nUpdated DataFrame:")
# print(students)
# TASK 5: Reading & Inspecting Data
# ============================================================

print("\n========== TASK 5: Reading & Inspecting Data ==========")

# Create a sample dataset
sales_data = pd.DataFrame({
    "Order_ID": [101, 102, 103, 104, 105,
                 106, 107, 108, 109, 110],

    "Product": [
        "Laptop",
        "Mouse",
        "Keyboard",
        "Monitor",
        "Laptop",
        "Mouse",
        "Headphones",
        "Monitor",
        "Keyboard",
        "Laptop"
    ],

    "Category": [
        "Electronics",
        "Accessories",
        "Accessories",
        "Electronics",
        "Electronics",
        "Accessories",
        "Accessories",
        "Electronics",
        "Accessories",
        "Electronics"
    ],

    "Region": [
        "West",
        "West",
        "South",
        "North",
        "South",
        "North",
        "West",
        "South",
        "North",
        "West"
    ],

    "Sales": [
        65000,
        1200,
        2500,
        18000,
        62000,
        1500,
        3500,
        17000,
        2200,
        68000
    ],

    "Quantity": [
        2, 5, 4, 2, 2,
        6, 3, 2, 4, 2
    ]
})

# Save dataset as CSV
sales_data.to_csv("sales_data.csv", index=False)

# Read CSV using Pandas
df = pd.read_csv("sales_data.csv")

print("First 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

# Number of rows and columns
print("\nNumber of Rows and Columns:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)

# Info
print("\nDataset Information:")
df.info()

#Describe
print("\nStatistical Description:")
print(df.describe())
# TASK 6: Selecting, Filtering & Sorting Data
# ============================================================

print("\n========== TASK 6: Selecting, Filtering & Sorting ==========")

# Select specific columns
print("Product and Sales Columns:")
print(df[["Product", "Sales"]])

#Select specific rows
print("\nFirst Three Rows:")
print(df.iloc[:3])

# Filter records
print("\nSales Greater Than 10,000:")
print(df[df["Sales"] > 10000])

# Multiple conditions
print("\nElectronics with Sales Greater Than 20,000:")

filtered_data = df[
    (df["Category"] == "Electronics") &
    (df["Sales"] > 20000)
]

print(filtered_data)

# Ascending order
print("\nSales in Ascending Order:")
print(df.sort_values(
    by="Sales",
    ascending=True
))

# Descending order
# print("\nSales in Descending Order:")
# print(df.sort_values(
#     by="Sales",
#     ascending=False
# ))
print("\n========== TASK 7: Handling Missing Values ==========")

# Dataset containing missing values
missing_data = pd.DataFrame({
    "Name": [
        "Amit",
        "Sneha",
        "Rahul",
        "Priya",
        "Neha"
    ],

    "Age": [
        20,
        21,
        np.nan,
        22,
        21
    ],

    "Marks": [
        85,
        np.nan,
        92,
        88,
        np.nan
    ],

    "City": [
        "Pune",
        "Mumbai",
        "Kolhapur",
        None,
        "Pune"
    ]
})

print("Dataset Before Handling Missing Values:")
print(missing_data)

# Identify missing values
print("\nMissing Values using isnull():")
print(missing_data.isnull())

# Count missing values
print("\nMissing Values in Each Column:")
print(missing_data.isnull().sum())

# Remove rows containing missing values
removed_data = missing_data.dropna()

print("\nAfter Removing Rows with Missing Values:")
print(removed_data)

# Fill missing values
filled_data = missing_data.copy()

filled_data["Age"] = filled_data["Age"].fillna(
    filled_data["Age"].mean()
)

filled_data["Marks"] = filled_data["Marks"].fillna(
    filled_data["Marks"].mean()
)

filled_data["City"] = filled_data["City"].fillna(
    "Unknown"
)

print("\nAfter Filling Missing Values:")
print(filled_data)

print("\nWhy Handling Missing Data is Important:")
print(
    "Handling missing data is important because it improves "
    "data quality, prevents errors, and helps produce reliable "
    "analysis and conclusions."
)
print("\n========== TASK 8: Merge, Concatenate, GroupBy & Pivot Table ==========")

# # ---------------- MERGE ----------------

employee_data = pd.DataFrame({
    "Employee_ID": [1, 2, 3, 4],
    "Name": ["Amit", "Sneha", "Rahul", "Priya"],
    "Department": [
        "IT",
        "HR",
        "IT",
        "Sales"
    ]
})

salary_data = pd.DataFrame({
    "Employee_ID": [1, 2, 3, 4],
    "Salary": [
        50000,
        45000,
        55000,
        48000
    ]
})

merged_data = pd.merge(
    employee_data,
    salary_data,
    on="Employee_ID"
)

print("\nMerged DataFrame:")
print(merged_data)


# ---------------- CONCATENATE ----------------

df1 = pd.DataFrame({
    "Name": ["Amit", "Sneha"],
    "Marks": [85, 90]
})

df2 = pd.DataFrame({
    "Name": ["Rahul", "Priya"],
    "Marks": [78, 88]
})

concatenated_data = pd.concat(
    [df1, df2],
    ignore_index=True
)

print("\nConcatenated DataFrame:")
print(concatenated_data)


# ---------------- GROUPBY ----------------

print("\nTotal Sales by Category:")

category_sum = df.groupby(
    "Category"
)["Sales"].sum()

print(category_sum)

print("\nAverage Sales by Category:")

category_mean = df.groupby(
    "Category"
)["Sales"].mean()

print(category_mean)

print("\nNumber of Orders by Category:")

category_count = df.groupby(
    "Category"
)["Order_ID"].count()

print(category_count)

print("\nMinimum Sales by Category:")

print(
    df.groupby("Category")["Sales"].min()
)

print("\nMaximum Sales by Category:")

print(
    df.groupby("Category")["Sales"].max()
)


# ---------------- PIVOT TABLE ----------------

pivot_table = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

print("\nPivot Table:")
print(pivot_table)

# TASK 9: Exporting Data
# ============================================================

print("\n========== TASK 9: Exporting Data ==========")

# Export final DataFrame to CSV
df.to_csv(
    "processed_sales_data.csv",
    index=False
)

print(
    "Data successfully exported to "
    "'processed_sales_data.csv'"
)

# Read exported file to verify
verified_data = pd.read_csv(
    "processed_sales_data.csv"
)

print("\nVerified Exported Data:")
print(verified_data)

print("\nExport Verification Successful!")

# TASK 10: Mini Data Analysis Project
# ============================================================

print("\n========== TASK 10: MINI DATA ANALYSIS PROJECT ==========")

# Load dataset
analysis_data = pd.read_csv(
    "sales_data.csv"
)

print("\n1. Dataset:")
print(analysis_data)


# ---------------- DATA INSPECTION ----------------

print("\n2. Data Inspection")

print("Shape:")
print(analysis_data.shape)

print("\nColumns:")
print(analysis_data.columns)

print("\nData Types:")
print(analysis_data.dtypes)


# ---------------- MISSING VALUES ----------------

print("\n3. Missing Values:")

print(
    analysis_data.isnull().sum()
)


# ---------------- SELECTING DATA ----------------

print("\n4. Selected Data:")

print(
    analysis_data[
        ["Product", "Sales"]
    ]
)


# ---------------- FILTERING ----------------

print("\n5. Sales Greater Than 20,000:")

high_sales = analysis_data[
    analysis_data["Sales"] > 20000
]

print(high_sales)


# ---------------- SORTING ----------------

print("\n6. Sales Sorted in Descending Order:")

sorted_data = analysis_data.sort_values(
    by="Sales",
    ascending=False
)

print(sorted_data)


# ---------------- GROUPBY ANALYSIS ----------------

print("\n7. Total Sales by Category:")

category_sales = analysis_data.groupby(
    "Category"
)["Sales"].sum()

print(category_sales)


print("\nAverage Sales by Region:")

region_sales = analysis_data.groupby(
    "Region"
)["Sales"].mean()

print(region_sales)


# ---------------- PIVOT TABLE ----------------

print("\n8. Pivot Table:")

analysis_pivot = pd.pivot_table(
    analysis_data,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

print(analysis_pivot)


# ---------------- INSIGHTS ----------------

print("\n9. KEY FINDINGS / INSIGHTS")

total_sales = analysis_data["Sales"].sum()

average_sales = analysis_data["Sales"].mean()

highest_sale = analysis_data["Sales"].max()

highest_sale_product = analysis_data.loc[
    analysis_data["Sales"].idxmax(),
    "Product"
]

highest_category = category_sales.idxmax()

highest_region = (
    analysis_data
    .groupby("Region")["Sales"]
    .sum()
    .idxmax()
)

print("Total Sales:", total_sales)

print(
    "Average Order Sales:",
    round(average_sales, 2)
)

print(
    "Highest Single Sale:",
    highest_sale
)

print(
    "Product with Highest Sale:",
    highest_sale_product
)

print(
    "Category with Highest Total Sales:",
    highest_category
)

print(
    "Region with Highest Total Sales:",
    highest_region
)


# ---------------- EXPORT FINAL DATA ----------------

analysis_data.to_csv(
    "final_processed_sales_data.csv",
    index=False
)

print(
    "\n10. Final processed dataset "
    "exported successfully."
)

print("\n================================================")
print("ALL 10 TASKS COMPLETED SUCCESSFULLY")
print("================================================")
