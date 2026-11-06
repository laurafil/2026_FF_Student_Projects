import pandas as pd

# '..' moves up one directory from 'raw' into your main project folder,
# then goes into the 'data' folder to find your file.
df = pd.read_csv("../data/trial_3d.csv")

print(df.head())