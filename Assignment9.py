# Assignment No. 9
# Implementation of Array Operations using NumPy and Pandas

import numpy as np
import pandas as pd

# ---------- NumPy Section ----------
print("=== NumPy Array Operations ===")

# 1. Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# 2. Array arithmetic operations
print("Addition:", arr + 5)
print("Subtraction:", arr - 5)
print("Multiplication:", arr * 2)
print("Division:", arr / 2)

# 3. Statistical operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 4. Reshaping array
arr2 = np.arange(1, 10).reshape(3, 3)
print("2D Array:\n", arr2)

# 5. Slicing array
print("Sliced Array (first 3 elements):", arr[:3])

# ---------- Pandas Section ----------
print("\n=== Pandas Operations ===")

# 1. Create a Pandas Series
series = pd.Series([10, 20, 30, 40, 50], index=['A', 'B', 'C', 'D', 'E'])
print("Series:\n", series)

# 2. Create a Pandas DataFrame
data = {
    'Name': ['Asha', 'Rahul', 'Sneha', 'Ravi'],
    'Age': [22, 25, 23, 24],
    'Marks': [88, 92, 79, 85]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# 3. Accessing columns and rows
print("\nAccessing 'Name' column:\n", df['Name'])
print("Accessing first two rows:\n", df.head(2))

# 4. Basic statistics
print("\nStatistical Summary:\n", df.describe())

# 5. Sorting and filtering
print("\nData sorted by Marks:\n", df.sort_values(by='Marks', ascending=False))

# 6. Adding a new column
df['Result'] = ['Pass' if m > 80 else 'Fail' for m in df['Marks']]
print("\nUpdated DataFrame with Result:\n", df)
