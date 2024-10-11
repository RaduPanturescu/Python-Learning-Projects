import random as r
import os

TO_backlog = {}
warehouse_inventory = {}
product_list = []
user = "TestUser1"

clear_console = lambda: os.system('cls')

def program_initialiser():
    clear_console()
    action = 0
    login = input("Username: ")
    

    
        # while login != user:
        #     print("try again")
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

def create_TO():        
    return

def remove_TO():
    return


def add_inventory(item, quantity):
    
    if item not in warehouse_inventory:
        warehouse_inventory[item] = quantity

    elif item in warehouse_inventory:
        stock = warehouse_inventory[item]
        warehouse_inventory[item] = stock + quantity 


def check_inventory():
    print(warehouse_inventory)

def pickting_TO():
    return



# add_inventory("Sol de Janeiro - Lip Balm", 25)
# add_inventory("Sol de Janeiro - Body Cream", 25)
# check_inventory()

program_initialiser()