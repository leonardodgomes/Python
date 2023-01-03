
# Read Excel with Python Pandas

# Read Excel files (extensions:.xlsx, .xls) with Python Pandas. To read an excel
# file as a DataFrame, use the pandas read_excel() method.

# You can read the first sheet, specific sheets, multiple sheets or all sheets. Pandas converts
# this to the DataFrame structure, which is a tabular like structure.


# Install xlrd

# Pandas. .read_excel a.) uses a library called xlrd internally.

# xlrd is a library for reading (input) Excel files (.xlsx, .xls) in Python.

# If you call pandas.read_excel s() in an environment where xlrd is not installed, you will receive an error message similar to the following:
#     ImportError: Install xlrd >= 0.9.0 for Excel support


import pandas as pd 

file_path = 'C:\\Users\\a070127\\Documents\\Leonardo\\Work\\Python\\03_Pandas\\00_Files\\data.xlsx'
sheet = 'Colors'

df = pd.read_excel(file_path)

print(df) 
