import random as r
import os

# product_code = {"Sol de Janeiro", 9400234596}
TO_backlog = {}
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

    TO_List = {}
    TO_number = r.randint(900000000,999999999)
    item = ""
    quantity = 0

    while True:
        if TO_number not in TO_backlog:
            TO_backlog[TO_number] = 1
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



add_inventory("Sol de Janeiro - Lip Balm", 25)
# add_inventory("Sol de Janeiro - Body Cream", 25)
# check_inventory()

# program_initialiser()
create_TO(3)