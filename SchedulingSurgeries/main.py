import pandas as pd
import surgery

all_surgeries = []

data = pd.read_csv("scheduled_surgeries.csv")

for surgery in data.itertuples():
    print(surgery[1])
    print(surgery[2])
    print(surgery[3])
    print(surgery[4])
    print(surgery[5])
    print("\n")
# print(data)
