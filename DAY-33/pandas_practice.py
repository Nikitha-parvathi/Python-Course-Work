import pandas as pd
import numpy as np


print("\n========== SERIES ==========")

# Create Series
marks = pd.Series([85, 90, 76, 92])
print("\nSeries:")
print(marks)

# Series with custom index
student_marks = pd.Series(
    [85, 90, 76, 92],
    index=["Alice", "Bob", "Cathy", "David"]
)

print("\nSeries with Custom Index:")
print(student_marks)

# Access Series value
print("\nBob's Marks:", student_marks["Bob"])

# Series operations
print("\nMarks + 5:")
print(student_marks + 5)

print("\nAverage:", student_marks.mean())
print("Maximum:", student_marks.max())
print("Minimum:", student_marks.min())
print("Total:", student_marks.sum())



print("\n========== DATAFRAME ==========")

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [18, 19, 17, 18, 20],
    "Marks": [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)



print("\n========== DATAFRAME INFORMATION ==========")

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nColumn Names:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Information:")
print(df.describe())

print("\nDataFrame Information:")
df.info()



print("\n========== SELECTING COLUMNS ==========")

# Single column
print("\nName Column:")
print(df["Name"])

# Multiple columns
print("\nName and Marks:")
print(df[["Name", "Marks"]])



print("\n========== SELECTING ROWS ==========")

# Using loc
print("\nRow with index 2:")
print(df.loc[2])

# Using iloc
print("\nSecond row:")
print(df.iloc[1])



print("\n========== SPECIFIC CELL ==========")

# loc
print("\nUsing loc:")
print(df.loc[1, "Marks"])

# iloc
print("\nUsing iloc:")
print(df.iloc[1, 2])



print("\n========== FILTERING ==========")

# Marks greater than 80
print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])

# Age equal to 18
print("\nStudents whose Age is 18:")
print(df[df["Age"] == 18])

# AND condition
print("\nMarks > 85 AND Age > 18:")
print(df[(df["Marks"] > 85) & (df["Age"] > 18)])

# OR condition
print("\nAge = 18 OR Marks > 90:")
print(df[(df["Age"] == 18) | (df["Marks"] > 90)])

# NOT EQUAL
print("\nStudents who are NOT 18:")
print(df[df["Age"] != 18])



print("\n========== isin() ==========")

print("\nStudents whose names are Bob or Eva:")
print(df[df["Name"].isin(["Bob", "Eva"])])



print("\n========== between() ==========")

print("\nStudents with Marks between 80 and 90:")
print(df[df["Marks"].between(80, 90)])



print("\n========== SPECIFIC ROWS AND COLUMNS ==========")

print("\nMarks of index 1 and 3:")
print(df.loc[[1, 3], "Marks"])



print("\n========== ADD COLUMN ==========")

df["Grade"] = ["A", "A+", "B", "A", "A+"]

print(df)



print("\n========== ADD ROW ==========")

new_row = {
    "Name": "Frank",
    "Age": 19,
    "Marks": 86,
    "Grade": "A"
}

df.loc[len(df)] = new_row

print(df)



print("\n========== DATA CLEANING ==========")

clean_data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Bob"],
    "Age": [25, np.nan, 30, 22, np.nan, 25],
    "City": ["Delhi", "Mumbai", np.nan, "Chennai", "Delhi", "Mumbai"]
}

clean_df = pd.DataFrame(clean_data)

print("\nOriginal Data:")
print(clean_df)



print("\n========== MISSING VALUES ==========")

print("\nisnull():")
print(clean_df.isnull())

print("\nnotnull():")
print(clean_df.notnull())



print("\n========== COUNT MISSING VALUES ==========")

print(clean_df.isnull().sum())



print("\n========== fillna() ==========")

filled_df = clean_df.fillna({
    "Age": 0,
    "City": "Unknown"
})

print(filled_df)



print("\n========== dropna() ==========")

dropped_df = clean_df.dropna()

print(dropped_df)



print("\n========== dropna(subset) ==========")

age_cleaned = clean_df.dropna(subset=["Age"])

print(age_cleaned)



print("\n========== replace() ==========")

replaced_df = clean_df.replace({
    "Delhi": "New Delhi",
    "Bob": "Robert"
})

print(replaced_df)



print("\n========== rename() ==========")

renamed_df = clean_df.rename(columns={
    "Name": "Student Name",
    "Age": "Student Age"
})

print(renamed_df)



print("\n========== astype() ==========")

type_data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": ["18", "19", "20"]
}

type_df = pd.DataFrame(type_data)

print("\nBefore:")
print(type_df.dtypes)

type_df["Age"] = type_df["Age"].astype(int)

print("\nAfter:")
print(type_df.dtypes)

print(type_df)




print("\n========== drop_duplicates() ==========")

print("\nBefore removing duplicates:")
print(clean_df)

duplicate_removed = clean_df.drop_duplicates()

print("\nAfter removing duplicates:")
print(duplicate_removed)



print("\n========== COMPLETE DATAFRAME ==========")

print(df)

print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumn Names:")
print(list(df.columns))

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

print("\nStudents who scored above 85:")
print(df[df["Marks"] > 85])

print("\n========== PROGRAM COMPLETED ==========")