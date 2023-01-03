import pandas as pd
import os
 
# Driver Code

path_folder = os.path.dirname(__file__)
print("Path: ",path_folder)

# Decide the two file paths according to your
# computer system
csvFilePath = path_folder + '/Datasets/Fiscal_Numbers.csv'
jsonFilePath = path_folder + '/Datasets/Fiscal_Numbers.json'
print("csvFilePath: ", csvFilePath)
print("jsonFilePath: ", jsonFilePath)


df = pd.read_csv (csvFilePath)
df.to_json (jsonFilePath)


