import pandas as pd
import supply as sp
data = pd.read_csv("MedicalSuppliesInventory.csv")

all_supplies = []


def get_cost_benefit(supply):
    return supply.cost_benefit


for supply in data.itertuples():
    new_supply = sp.Supply(supply[1], int(supply[2]), int(supply[3]), int(supply[4]))
    all_supplies.append(new_supply)

all_supplies.sort(key=get_cost_benefit)

for supply in all_supplies:
    supply.print_data()
