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
        price = float(input("What is the price of the item? "))
        shopping_cart.append((item, price))
        print(f"'{item}' has been added to the cart for ${price:.2f}.\n")
        
    elif action == 2:
        print("The contents of the shopping cart are:")
        for i, item in enumerate(shopping_cart):
            print(f"{i+1}. {item[0]} - ${item[1]:.2f}")
        print("")
        
    elif action == 3:
        item = input("What item would you like to remove? ")
        try:
            index = int(item) - 1
            if index >= 0 and index < len(shopping_cart):
                removed_item = shopping_cart.pop(index)
                print(f"'{removed_item[0]}' has been removed from the cart.\n")
            else:
                print("Invalid item number. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            
    elif action == 4:
        total_price = sum(price for _, price in shopping_cart)
        print(f"The total cost of the items in the cart is ${total_price:.2f}.\n")
        
    elif action == 5:
        print("Thank you. Goodbye.")
        break
        
    else:
        print("Invalid action. Please try again.\n")