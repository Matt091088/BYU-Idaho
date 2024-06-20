import csv
import os
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    compound_dict = {}
    absolute_path = 'C:/Users/ferna/Desktop/BYU Idaho/cse111/week9/'

    with open(os.path.join(absolute_path, filename), newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        for row in reader:
            key = row[key_column_index]
            compound_dict[key] = row
    return compound_dict

def print_receipt(products_dict, requested_items):
    print("\nInkom Emporium\n")

    for item, details in requested_items.items():
        quantity = details['quantity']
        price = details['price']
        print(f"{item}: {quantity} @ {price:.2f}")

    num_items = sum(details['quantity'] for details in requested_items.values())
    subtotal = sum(details['quantity'] * details['price'] for details in requested_items.values())
    sales_tax_rate = 0.06
    sales_tax = subtotal * sales_tax_rate
    total = subtotal + sales_tax

    print(f"\nNumber of Items: {num_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}\n")
    
    print("Thank you for shopping at the Inkom Emporium.")
    
    # Get the current date and time
    current_date_and_time = datetime.now()
    print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))

def main():
    try:
        # Call read_dictionary function and store the compound dictionary in products_dict
        products_dict = read_dictionary("products.csv", 0)

        # Imprime la ruta absoluta para depuración
        absolute_path = 'C:/Users/ferna/Desktop/BYU Idaho/cse111/week9/'
        print("Absolute Path:", absolute_path)

        # Open request.csv file for reading
        requested_items = {}
        with open(os.path.join(absolute_path, "request.csv"), newline='') as request_file:
            reader = csv.reader(request_file)

            # Skip the first line of the request.csv file
            next(reader)

            # Process each row in the request.csv file
            for row in reader:
                product_number = row[0]

                # Check if the product_number is in products_dict
                if product_number in products_dict:
                    product_info = products_dict[product_number]
                    product_name = product_info[1]
                    quantity = int(row[1])
                    price = float(product_info[2])

                    # Update requested_items dictionary
                    requested_items[product_name] = {'quantity': quantity, 'price': price}

        # Call the print_receipt function
        print_receipt(products_dict, requested_items)

    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file\n'{e}'")

# Call the main function only if the script is executed directly
if __name__ == "__main__":
    main()


