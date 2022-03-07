import smtplib

import pandas as pd
import supply as sp
data = pd.read_csv("MedicalSuppliesInventory.csv")

all_supplies = []


def send_email(subject, message):

    gmail_user = ''
    gmail_password = ''
    to = ''
    body = message.replace('\n','<br>')

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(gmail_user, to, f"Subject:Buy List\n\n{message}")

        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)


def get_cost_benefit(supply):
    return supply.cost_benefit


for supply in data.itertuples():
    new_supply = sp.Supply(supply[1], int(supply[2]), int(supply[3]), int(supply[4]))
    all_supplies.append(new_supply)

all_supplies.sort(key=get_cost_benefit)

all_supplies.reverse()

i = 0
with open('buy_list.txt', 'w+') as f:
    f.write(" - PRIORITY PURCHASE LIST - \n")
    for supply in all_supplies:
        f.write(f"\nSupply {i+1}\n")
        f.write("%s\n" % supply.return_data())
        i += 1

with open('buy_list.txt') as f:
    lines = f.readlines()
    send_email("Buy list", ' '.join(lines))
    #print(lines)
