"""
Program: Warehouse control
Author: Ivan Ramirez
Functionality:
    - Register Items
        - id (auto generated): int
        - title: str
        - category: str
        - stock: int
        - price: float
"""

# imports

from menu import print_menu, clear, print_header, print_item, print_table
from item import Item

# global vars

catalog = []

# functions



def register_item():
    clear()
    print_header(" Register new Item ")
    title = input("Please provide the Title: ")
    category = input("Please provide the Category: ")
    stock = int(input("Please provide the Stock: "))
    price = float(input("Please provide the Price: "))

    the_item = Item(1,title,category,stock,price)

    # add the obj to the list

    catalog.append(the_item)

    print("\n  Item saved, you have " + str(len(catalog)) + " items in your catalog")

def display_catalog():
    clear()
    print_header(" Catalog ")
    if(len(catalog) == 0):
        print(" ** No items to display")
    else:
        for item in catalog :
            print_item(item)

def display_items_out_of_stock():
    clear()
    print_header(" Items out of stock ")
    if(len(catalog) == 0):
        print(" ** No items to display")
    else:
        for item in catalog:
            if(item.stock == 0):
                print_item(item)

def total_stock_value():
    clear()
    print_header(" Total stock value ")
    total = 0.0
    for item in catalog:
        total += item.stock * item.price
    print("The total is: $" + str(total))


# instructions
opc = ""
while( opc != "x" ):
    print_menu()
    opc = input("\nPlease select an option: ")

    if(opc == "1"):
        register_item()
    elif(opc == "2"):
        # create a function, call, travel the list and display the item title
        display_catalog()
    elif(opc == "3"):
        display_items_out_of_stock()
    elif(opc == "4"):
        total_stock_value()

    if(opc != "x"):
        input("\nPress any key to continue...")
print("Good bye!")