from os import system, name 
import datetime

def print_header (title):
    print("-" * 67)
    print("  " + title + "  ")
    print("-" * 67)

def clear():
     # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def print_menu():
    clear()
    print("-" * 67)
    print("    Warehouse control  " + (" " * 15) + "[" + get_date_time() + "]")
    print("-" * 67)

    # print_header("Warehouse control")
    print("[1] Register new Item")
    print("[2] Display Catalog")
    print("[3] Display items out of stock")
    print("[4] Stock value")
    print("[5] Update price")
    print("[6] Delete item")
    print("[7] Update item stock")
    print("[8] Print Categories")
    print("[9] Cheapest product")
    print("[10] 3 most expensive products")
    print("[x] Close")


def get_date_time():
    now = datetime.datetime.now()
    return now.strftime("%d/%b/%Y %T")


def print_item(item):
    print (
        str(item.id).rjust(3) 
        + " | " + item.title.ljust(20) 
        + " | " + item.category.ljust(12) 
        + " | " + str(item.stock).rjust(8)
        + " | $" + str(item.price).rjust(12)
    )