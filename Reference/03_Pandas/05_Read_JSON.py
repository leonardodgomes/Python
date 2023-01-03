# Read JSON
# Big data sets are often stored, or extracted as JSON.
# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

# Example, Load the JSON file into a DataFrame:

import pandas as pd

df = pd.read_xml('\\fileshare.ageas.pt\\Plataforma Vida\\P&BA\\Data Science\\questionarios\\env\\SOURCE\\PRTVIDA_QUESTS_1 - LG.xml')
                   
print(df.to_string()) # Tip: use to_string() to print the entire DataFrame.
