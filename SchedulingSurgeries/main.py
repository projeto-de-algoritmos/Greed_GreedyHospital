import pandas as pd
import surgery as sg

all_surgeries = []
optimal_schedule = []


def get_end_time(surgery):
    return surgery.end_time


data = pd.read_csv("scheduled_surgeries.csv")

for surgery in data.itertuples():
    start_time = ( (int(surgery[3][:2])) * 24) + int(surgery[4][:2])
    end_time = start_time + int(surgery[5])
    new_surgery = sg.Surgery(surgery[1], surgery[2], start_time, end_time)
    all_surgeries.append(new_surgery)

#Sort jobs by end time
all_surgeries.sort(key=get_end_time)

surgery_number = 0
A = all_surgeries[0]

for surgery in all_surgeries:
    if surgery_number == 0:
        optimal_schedule.append(surgery)
        A = surgery
    else:
        if surgery.start_time >= A.end_time:
            optimal_schedule.append(surgery)
            A = surgery
    surgery_number += 1

for optimal in optimal_schedule:
    print(optimal.print_data())
