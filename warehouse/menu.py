from os import system, name 

def print_header (title):
    print("-" * 30)
    print("  " + title + "  ")
    print("-" * 30)

def clear():
     # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def print_menu():
    clear()
    print_header("Warehouse control")
    print("[1] Register new Item")
    print("[2] Display Catalog")
    print("[3] Display items out of stock")
    print("[4] Stock value")
    print("[x] Close")

def print_item(item):
    print (
        str(item.id) 
        + " | " + item.title 
        + " | " + item.category 
        + " | " + str(item.stock)
        + " | " + str(item.price)
    )