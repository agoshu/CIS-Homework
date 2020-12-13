#Abel Goshu
#1675552

import csv
from datetime import date

import pandas as pd


def create_full_inventory():
    # Takes data from CSV files
    df_manufacturer = pd.read_csv('ManufacturerList.csv', header=None, index_col=0)
    df_price = pd.read_csv('PriceList.csv', header=None, index_col=0)
    df_dates = pd.read_csv('ServiceDatesList.csv', header=None, index_col=0)
    df_manufacturer_info = df_manufacturer.iloc[:, 0:2]
    df_damaged = df_manufacturer[3]

    # Joins the necessary data
    df_joined = df_manufacturer_info.join(df_price, how='inner', rsuffix='price')
    df_joined = df_joined.join(df_dates, how='inner', rsuffix='dates')
    df_joined = df_joined.join(df_damaged, how='inner', rsuffix='damaged')

    # Sorts the values by Manufacturer and type and exports to new CSV
    df_buffer = df_joined.rename(columns={'1': 'Manufacturer', 2: 'Type', '1price': 'price', 1: 'date', 3: 'condition'})
    df_sort = df_buffer.sort_values(by=["Manufacturer", "Type"])
    print(df_sort)
    df_sort.to_csv('FullInventory.csv', header=None)


def create_csv_inventory():
    # Reads data and puts into data array
    data = []
    with open('FullInventory.csv') as inventory:
        reader = csv.reader(inventory)
        for row in reader:
            data.append(row)


    # Strings used to search
    laptop_string = "laptop"
    phone_string = "phone"
    tower_string = "tower"

    col = [x[2] for x in data]

    # Arrays to hold information for each type
    laptop = []
    phone = []
    tower = []


    # Searches for laptop
    if laptop_string in col:
        for x in range(0, len(data)):
            if laptop_string == data[x][2]:
                laptop.append(data[x])


    # Searches for phone
    if phone_string in col:
        for x in range(0, len(data)):
            if phone_string == data[x][2]:
                phone.append(data[x])

    # Searches for tower
    if tower_string in col:
        for x in range(0, len(data)):
            if tower_string == data[x][2]:
                tower.append(data[x])

    # Sorts the array for each item
    df_laptop = pd.DataFrame(laptop)
    df_laptop = df_laptop.sort_values(by=[0])
    del df_laptop[2]
    print(df_laptop)

    df_phone = pd.DataFrame(phone)
    df_phone = df_phone.sort_values(by=[0])
    del df_phone[2]
    print(df_phone)

    df_tower = pd.DataFrame(tower)
    df_tower = df_tower.sort_values(by=[0])
    del df_tower[2]
    print(df_tower)

    # Prints the data from each item array into their own CSV
    df_laptop.to_csv('LaptopInventory.csv', header=None, index=False)
    df_phone.to_csv('PhoneInventory.csv', header=None, index=False)
    df_tower.to_csv('TowerInventory.csv', header=None, index=False)


def item_service_date():
    # Reads data and puts into data array
    data = []
    with open('FullInventory.csv') as inventory:
        reader = csv.reader(inventory)
        for row in reader:
            data.append(row)

    # Sorts data by service date
    df_inventory = pd.DataFrame(data)
    today = date.today()
    today = today.strftime("%m/%d/%Y")
    df_inventory[4] = pd.to_datetime(df_inventory[4])
    before_end_date = df_inventory[4] < today
    filtered_dates = df_inventory.loc[before_end_date]
    df_sort = filtered_dates.sort_values(by=[4])
    print(df_sort)
    # Prints the data to CSV file
    df_sort.to_csv('PastServiceDateInventory.csv', header=None, index=False)


def damaged_items():
    # Reads data and puts into data array
    data = []
    with open('FullInventory.csv') as inventory:
        reader = csv.reader(inventory)
        for row in reader:
            data.append(row)

    # Searches for damaged and places info into array
    col = [x[5] for x in data]
    damage_string = "damaged"
    damaged = []
    if damage_string in col:
        for x in range(0, len(data)):
            if damage_string == data[x][5]:
                damaged.append(data[x])

    # Sorts damaged array and prints to CSV
    df_damaged = pd.DataFrame(damaged)
    df_damaged[3] = pd.to_numeric(df_damaged[3])
    df_sort = df_damaged.sort_values(by=[3])
    print(df_sort)
    df_sort.to_csv('DamagedInventory.csv', header=None, index=False)



create_full_inventory()
create_csv_inventory()
item_service_date()
damaged_items()

#Asking user input

usermanu = str(input("Enter your manufacturer: "))
usertype = str(input("Please enter your item type: "))
itemm = []
while (usermanu != "q"):
    for x in range(0, len(create_full_inventory)):
        if usermanu in create_full_inventory[x] and usertype in create_full_inventory[x]:
            itemm.append(create_full_inventory[x])
    if len(itemm) != 0:
        your_item = sorted(itemm, key=itemgetter, reverse=True)
        print("Your Item is: ", your_item[0])
    else:
        print("No such item in Inventory")

    usermanu = str(input("Enter your manufacturer, or q to exit query:"))
    usertype = str(input("Please enter your item type: "))
