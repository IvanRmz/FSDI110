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

from menu import print_menu, clear, print_header, print_item
from item import Item
import pickle
# global vars

catalog = []
last_id = 0
data_file = "warehouse.data"
price_opc = "price"
stock_opc = "stock"

# functions

def serialize_catalog():
    global data_file
    write = open(data_file, "wb") # wb == create/overwrite the file
    pickle.dump(catalog, write)
    write.close() 
    print("Data saved!")

def deserialize_catalog():
    global data_file
    global last_id
    try:
        reader = open(data_file, "rb") # rb == read binary, throw exception if file doesn't exist
        temp_list = pickle.load(reader)
        for item in temp_list:
            catalog.append(item)

        last = catalog[-1]
        last_id = last.id + 1
        print("Deserialized " + str(len(catalog)) + " items")
    except:
        print("File doesn't exist, data not loaded")
    

def register_item():
    global last_id
    clear()
    try:
        print_header(" Register new Item ")
        title = input("Please provide the Title: ")
        category = input("Please provide the Category: ")
        stock = int(input("Please provide the Stock: "))
        price = float(input("Please provide the Price: "))

        the_item = Item(last_id,title,category,stock,price)
        last_id+=1
        # add the obj to the list

        catalog.append(the_item)

        print("\n  Item saved, you have " + str(len(catalog)) + " items in your catalog")
        serialize_catalog()
    except ValueError:
        print("*Error, provide valid numbers!")
    except:
        print("*Error, verify data and try again!")

def display_catalog():
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

def update_item(option):
    global price_opc
    global stock_opc
    id_found = False
    display_catalog()
    try:
        id = int(input("Choose Id of the item to change: "))
        for item in catalog:
            if(id == item.id):
                id_found = True
                try: 
                    if(option == price_opc):
                        new_price = float(input("Insert new price: "))
                        item.price = new_price
                    elif(option == stock_opc):
                        new_stock = float(input("Insert new stock: "))
                        item.stock = new_stock

                    serialize_catalog()
                    print("\n ~~~ Item updated successfully ~~~ \n")
                    display_catalog()
                    break
                except ValueError:
                    print("*Error, the new price has to be a number, please try again!")
        if(not id_found):
            print("Id not found, choose a correct Id from the list")
    except ValueError:
        print("*Error, the Id has to be a number, please try again!")

def delete_item():
    item_found = False
    display_catalog()
    item_to_remove = Item
    try:
        id = int(input("Choose Id of the item to delete: "))
        for item in catalog:
            if(id == item.id):
                item_found = True
                item_to_remove = item
                break
        if(not item_found):
            print("Id not found, choose a correct Id from the list")
        else:
            catalog.remove(item_to_remove) 
            serialize_catalog()
            print("\n ~~~ Item removed successfully ~~~ \n")
            display_catalog()
    except ValueError:
        print("*Error, the Id has to be a number, please try again!")


def display_categories():
    clear()
    print_header("  Categories  ")
    categories = []
    for item in catalog:
        if( item.category.lower() not in (category.lower() for category in categories) ):
            categories.append(item.category)
            print(item.category)

    if(len(categories) == 0):
        print("*** No categories to display ***")

def cheapest_product():
    clear()
    print_header("  Cheapest Product  ")
    if(len(catalog) == 0):
        print("*** No products in the catalog ***")
    else:
        cheapest_item = catalog[0]
        for item in catalog:
            if(item.price < cheapest_item.price ):
                cheapest_item = item
        print("The Cheapest product it is:")
        print_item(cheapest_item)

def three_expensive_products():
    clear()
    print_header("  3 most expensive products  ")
    temp = []
    if(len(catalog) == 0):
        print("*** No products in the catalog ***")
    else:
        temp  = sorted(catalog, key=lambda x: x.price, reverse=True)
        count = 0
        for item in temp:
            print_item(item)
            count+=1
            if(count == 3):
                break
       


    
        

# instructions
deserialize_catalog()
input("\nPress Enter to continue...")

opc = ""
while( opc != "x" ):
    print_menu()
    opc = input("\nPlease select an option: ")

    if(opc == "1"):
        register_item()
    elif(opc == "2"):
        # create a function, call, travel the list and display the item title
        clear()
        print_header(" Catalog ")
        display_catalog()
    elif(opc == "3"):
        display_items_out_of_stock()
    elif(opc == "4"):
        total_stock_value()
    elif(opc == "5"):
        clear()
        print_header(" Update Price ")
        update_item(price_opc)
    elif(opc == "6"):
        clear()
        print_header(" Delete Item ")
        delete_item()
    elif(opc == "7"):
        clear()
        print_header(" Update Item Stock ")
        update_item(stock_opc)
    elif(opc == "8"):
        display_categories()
    elif(opc == "9"):
        cheapest_product()
    elif(opc == "10"):
        three_expensive_products()

    if(opc != "x"):
        input("\nPress Enter to continue...")
print("Good bye!")