import pandas as pd
import surgery as sg

all_surgeries = []
# this will contain the rooms
rooms = []
first_room = []
rooms.append(first_room)


def get_start_time(surgery):
    return surgery.start_time

data = pd.read_csv("scheduled_surgeries.csv")

for surgery in data.itertuples():
    start_time = ( (int(surgery[3][:2])) * 24) + int(surgery[4][:2])
    end_time = start_time + int(surgery[5])
    new_surgery = sg.Surgery(surgery[1], surgery[2], start_time, end_time)
    all_surgeries.append(new_surgery)

# sort jobs by start time
all_surgeries.sort(key=get_start_time)

for sorted_surgery in all_surgeries:
    sorted_surgery.print_data()
