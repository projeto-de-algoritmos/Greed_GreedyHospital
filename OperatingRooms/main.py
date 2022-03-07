import pandas as pd
import surgery as sg

all_surgeries = []

# this will contain the rooms, the hospital has 10 rooms max, and we want to user the minimum amount possible
rooms = [[], [], [], [], [], [], [], [], [], []]


def get_start_time(surgery):
    return surgery.start_time


def add_to_free_room(surgery_to_add, room_number):

    if not rooms[room_number]:
        rooms[room_number].append(surgery_to_add)

    else:
        if rooms[room_number][ len(rooms[room_number]) - 1].end_time <= surgery_to_add.start_time:
            rooms[room_number].append(surgery_to_add)
        else:
            add_to_free_room(surgery_to_add, room_number + 1)

data = pd.read_csv("scheduled_surgeries.csv")

for surgery in data.itertuples():
    start_time = ( (int(surgery[3][:2])) * 24) + int(surgery[4][:2])
    end_time = start_time + int(surgery[5])
    new_surgery = sg.Surgery(surgery[1], surgery[2], start_time, end_time)
    all_surgeries.append(new_surgery)

# sort jobs by start time
all_surgeries.sort(key=get_start_time)

i = 0

for sorted_surgery in all_surgeries:
    if i == 0:
        rooms[0].append(sorted_surgery)
    else:
        add_to_free_room(sorted_surgery, 0)
    i += 1


i = 0
for room in rooms:
    if room:
        with open(f'room_{i+1}_schedule.txt', 'w+') as f:
            for procedure in room:
                f.write(procedure.return_data())
    i += 1
