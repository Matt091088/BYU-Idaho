print ("Welcome to MC Food!")

print ("Can I take your order?")

childrenmeal = float(input("What is the price of a child's meal?"))
adultmeal = float(input("What is the price of a adult's meal?"))
number_of_children = int(input("How many children are there?"))
number_of_adults = int(input("How many adults are there?"))
sale_tax_rates = float(input("What is the sale tax rates?"))


subtotal = (int (number_of_children) * float (childrenmeal) + int (number_of_adults) * float (adultmeal))

sale_tax = float (subtotal*sale_tax_rates/100)
total_cost = subtotal + sale_tax

print (f"Subtotal ${subtotal:.2f}")
print (f"Sale Tax ${sale_tax:.2f}")
print (f"Total Cost ${total_cost:.2f}")


payment = float(input("What is the payment amount?"))
change = (payment-total_cost)
print(f"Your change is:${change:.2f}")
#extra requirements#
print("Thank you for shopping with us!")
