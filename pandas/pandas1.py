import pandas as pd
import math

filename = "./astronauts.csv"

# df = dataframe
df = pd.read_csv(filename, delimiter=",")    # delimiter="," is default

print(df.head())
print(len(df))
print(df.iloc[0])          # horizontal slicing

print("*** ACCESS COLUMN ***")

col_names = df["Name"]     # access col / vertical slicing
i = 0
for name in col_names:
    print("{} {}".format(i,name))
    i = i + 1
    if i >= 4:
        break

e1 = df.iloc[0]                                          # get first data element
print("Name='{}'".format(e1["Name"]))                    # access cols of data element
print("Birth Date='{}'".format(e1["Birth Date"]))
print("***")
 
subs = df.iloc[4:8]            # horizontal slicing
names = subs["Name"]
print(names)

print("*** ITERATE ***")

for row in df.iterrows():        # how to iterate over rows
    (pos, dataitem) = row
    print("{}\t'{}'\t{}".format(pos, dataitem["Name"], dataitem["Space Flights"]))
    if pos >= 5:
        break

print("*** FILTER ***")

df_before_1960 = df[df["Year"] < 1960]
print(df_before_1960)

df_mission_deaths = df[not math.isnan(df["Death Mission"])]
print(df_mission_deaths)

