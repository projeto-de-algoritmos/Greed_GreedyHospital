import pandas as pd
import surgery as sg

all_surgeries = []

data = pd.read_csv("scheduled_surgeries.csv")

for surgery in data.itertuples():
    start_time = (int(surgery[3][:2])) * int(surgery[4][:2])
    end_time = start_time + int(surgery[5])
    new_surgery = sg.Surgery(surgery[1], surgery[2], start_time, end_time)
    all_surgeries.append(new_surgery)

for surgery in all_surgeries:
    surgery.print_data()
