shopping_cart = []

while True:
    print("Welcome to the Shopping Cart Program!\n")
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit\n")
    
    action = int(input("Please enter an action: "))
    
    if action == 1:
        item = input("What item would you like to add? ")
        shopping_cart.append(item)
        print(f"'{item}' has been added to the cart.\n")
        
    elif action == 2:
        print("The contents of the shopping cart are:")
        for item in shopping_cart:
            print(item)
        print("")
        
    elif action == 3:
        item = input("What item would you like to remove? ")
        if item in shopping_cart:
            shopping_cart.remove(item)
            print(f"'{item}' has been removed from the cart.\n")
        else:
            print(f"'{item}' is not in the cart.\n")
            
    elif action == 4:
        print(f"The total cost of the items in the cart is ${len(shopping_cart) * 10}.\n")
        
    elif action == 5:
        print("Thank you. Goodbye.")
        break
        
    else:
        print("Invalid action. Please try again.\n")