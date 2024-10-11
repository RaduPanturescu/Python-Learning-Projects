import random as r
import os

TO_backlog = {}
warehouse_inventory = {}
product_list = []
user = "TestUser1"


def program_initialiser():
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



add_inventory("Sol de Janeiro - Lip Balm", 25)
add_inventory("Sol de Janeiro - Lip Balm", 25)
add_inventory("Sol de Janeiro - Lip Balm", 25)
add_inventory("Sol de Janeiro - Booty Balm", 25)


check_inventory()