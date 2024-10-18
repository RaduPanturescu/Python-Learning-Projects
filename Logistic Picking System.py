import random as r
import os
from datetime import datetime
import time

# product_code = {"Sol de Janeiro", 9400234596}
TO_backlog = {"938240750":1}
warehouse_inventory = {}
product_list = []
user = "TestUser1"

test_order_1 = {"Sol de Janeiro": 5,
                "Gucci Flora": 1,
                "Prada Paradox": 1} 

clear_console = lambda: os.system('cls')


# Main loop program where the user can perform actions
def program_initialiser():
    clear_console()
    action = 0
    login = input("Username: ")
    
    if login == user:
        while True:
            print(f"Welcome {user}!")
            print("------------------")
            print("")
            action = int(input("Select a program: - (1) Add Inventory -- (2) Check Inventory   "))
            if action == 1:
                item = input("What item to add to inventory  -  ")
                quantity = int(input("How many units  -  "))
                add_inventory(item, quantity)

            elif action == 2:
                check_inventory()    
    return

# Create an order as a customer for the picking system
def create_TO(picking_quantity): 

    TO_number = r.randint(900000000,999999999)
    item = ""
    quantity = 0

    while True:
        if TO_number not in TO_backlog:
            for TO in TO_backlog:
                # TO_backlog[TO_number] = int(TO)+1   XXXXX
                print("ok")
                print(TO_backlog)
            break 
        else:
            TO_number = r.randint(900000000,999999999)
            
    for i in range(picking_quantity):
        if item not in TO_backlog:
            item = input("Item to order - ")
            quantity = input("How many? - ")
            TO_backlog[item] = quantity

        if item in TO_backlog:
            stock = TO_backlog[item]
            TO_backlog[item] = stock + quantity

    print(TO_backlog)
    print(TO_number)
   

# Delete an order
def remove_TO():
    return

# Add item to the main stock inventory with quantity
def add_inventory(item, quantity):
    
    if item not in warehouse_inventory:
        warehouse_inventory[item] = quantity

    elif item in warehouse_inventory:
        stock = warehouse_inventory[item]
        warehouse_inventory[item] = stock + quantity 

# Displays the current inventory
def check_inventory():
    print(warehouse_inventory)


def pickting_TO():
    return


class TO:
    def __init__(self, creation_date, to_code, order_products, order_quantity):
        self.self = self
        self.date = creation_date
        self.code = to_code
        self.products = order_products
        self.quantity = order_quantity
        if self not in TO_backlog:
            TO_backlog[self] = to_code
        else:
            return "Error"

    def print_TO(self):
        print(f"""TO Created at - {self.date}
TO code - {self.code}
Products ordered - {self.products}
Ammount ordered - {self.quantity}""")
    
    def delete_TO(self):
        TO_backlog.pop(self)
    

TO1 = TO(datetime.fromtimestamp(time.time()), r.randint(0,1000), "Sol de janeiro", r.randint(1,10))
time.sleep(2)
TO2 = TO(datetime.fromtimestamp(time.time()), r.randint(0,1000), "Sol de janeiro", r.randint(1,10))

TO.print_TO(TO1)
TO.print_TO(TO2)
print(TO_backlog)