import math
from datetime import datetime

# Read the three numbers for the tire from the keyboard
width = float(input("Enter the width of the tire in mm: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))

# Calculate the volume of space inside the tire
volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000)

current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Display the result
print(f"The approximate volume is {volume: .2f} liters")

with open('C:/Users/ferna/Desktop/BYU Idaho/cse111/week1/volumes.txt', 'a') as file:


    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}\n")

print("Data has been saved to 'volumes.txt'.")


# ask the user if they want to buy it
buy_tires = input("Do you want to buy tires with these dimensions? (yes/no): ").strip().lower()

if buy_tires == "yes":
    phone_number = input("Please enter your phone number: ")
    
    with open('C:/Users/ferna/Desktop/BYU Idaho/cse111/week1/volumes.txt', 'a') as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}, {phone_number}\n")

    print("Thank you! Your phone number has been saved.")
else:
    print("Thank you for using the tire volume calculator.")
