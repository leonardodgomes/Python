
import pandas as pd
import os


path_folder = os.path.dirname(__file__)+'/Datasets/'
file_name = 'Fiscal_Numbers.csv'
path = path_folder+file_name


print('-------Base Dataframe')
df = pd.read_csv(path, sep=';')
print(df.to_string())


#Create the two two columns with the mask for the ID and Fiscal Number
new_df = df #Create a new dataframe just for comparison.
new_df.insert(0, 'New_ID', range(880, 880 + len(df)))
new_df['New_Fiscal_Number'] = range(100000000, 100000000+len(df))

new_df.drop(columns=['ID', 'Fiscal_number'], axis=1, inplace=True)

print('-------New dataframe with data annonymization')
print(new_df.to_string())