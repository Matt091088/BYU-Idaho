import csv

# I found this on internet and I think it would be very cool to add as an extra to show creativity.
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
reset = "\033[0m"

with open('life-expectancy.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    
    min_life_exp = float('inf')
    max_life_exp = float('-inf')
    min_year = ''
    max_year = ''
    min_country = ''
    max_country = ''
    for row in reader:
        year = row['Year']
        country = row['Entity']
        life_exp = float(row['Life expectancy (years)'])
        if life_exp < min_life_exp:
            min_life_exp = life_exp
            min_year = year
            min_country = country
        if life_exp > max_life_exp:
            max_life_exp = life_exp
            max_year = year
            max_country = country

    
    print(green + f"The overall max life expectancy is: {max_life_exp:.2f} from {max_country} in {max_year}" + reset)
    print(red + f"The overall min life expectancy is: {min_life_exp:.2f} from {min_country} in {min_year}" + reset)

    
    year = input("Enter the year of interest: ")
    total_life_exp = 0
    count = 0
    min_life_exp = float('inf')
    max_life_exp = float('-inf')
    min_country = ''
    max_country = ''
    
    csvfile.seek(0)
    next(reader)
    for row in reader:
        if row['Year'] == year:
            life_exp = float(row['Life expectancy (years)'])
            total_life_exp += life_exp
            count += 1
            if life_exp < min_life_exp:
                min_life_exp = life_exp
                min_country = row['Entity']
            if life_exp > max_life_exp:
                max_life_exp = life_exp
                max_country = row['Entity']
    avg_life_exp = total_life_exp / count

    # it will Print the results for the user's selected year, with different colors
    print(yellow + f"\nFor the year {year}:" + reset)
    print(f"The average life expectancy across all countries was {avg_life_exp:.2f}")
    print(green + f"The max life expectancy was in {max_country} with {max_life_exp:.2f}" + reset)
    print(red + f"The min life expectancy was in {min_country} with {min_life_exp:.3f}" + reset)
