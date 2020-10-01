import datetime

def print_menu():
    print("-" * 20)
    print("   Python Calc    ")
    print("-" * 20)

    print("[1] Add")
    print("[2] Substract")
    print("[3] Multiply")
    print("[4] Division")
    print("[5] My age")
    print("[x] Exit/Close")


"""
 opc = 5
 ask for the  year of birth
 tell the age

"""

# instruction
opc = ""
while ( opc != "x" ):
    print_menu()

    opc = input("\nPlease choose an option: ")
    if( opc >= "1" and opc <= "4"):
        num1 = float(input("First number: "))
        num2 = float(input("Second number: ")) 
        if( opc == "1" ):   
            res = num1 + num2
            print("\n")
        elif( opc == "2" ):
            res = num1 - num2
        elif( opc == "3" ):
            res = num1 * num2
        elif( opc == "4" ):
            if(num2 == 0):
                print("**Error, don't allowed to divide by 0")
                print("\n")
                continue
            else:
                res = num1 / num2
        print("Result: " + str(res))
        print("\n")
    if( opc == "5" ):
        yearBirth = int(input("Insert your year of birth: "))
        now = datetime.datetime.now()
        res = now.year - yearBirth
        print("You have " + str(res) + " years old")
        print("\n")

print("Good bye!!!")