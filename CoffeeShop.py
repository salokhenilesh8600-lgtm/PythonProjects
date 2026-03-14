menu = {
"pizza":120,
"burger": 30,
"coffee":10,
"chowmein":30,
"maggie":40,
"dosa": 60,
}

a = input("Hello, sir\nWhat Help do you want?\n")

def order():
    total_order = 0
    if a == "order":
        b = input("What would you like to order?\n")
        if b in menu:
            total_order += menu[b]
            print(f"{b} has been added to your list")
        else:
            print("We dont have that item sir")
            
        
        c = input("Want Anything else?\n")
        
        if c == 'yes':
            d = input("What do you want?\n")
            if d in menu:
                total_order += menu[d]
                print(f"{d} has been added to your list")
                print(f"your Total bill is {total_order}")
            else:
                print("We dont have that sir")
        elif c == 'no':
            print(f"Your total bill is {total_order}")       
            
        if total_order == 0:
            print("Must buy something whenever you visit next time")
    elif a == "list":
        print("___ARISE RESTU MENU___")
        print("1. pizza - 120₹\n2. burger - 30₹\n3. coffee - 10₹\n3. chowmein - 30₹\n4. maggie - 40₹\n5. dosa - 60₹")                 
        
order()