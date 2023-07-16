import csv

lowest = float('inf')
highest = float('-inf')

with open('life-expectancy.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        life_expectancy = float(row[3])
        if life_expectancy < lowest:
            lowest = life_expectancy
        if life_expectancy > highest:
            highest = life_expectancy

print(f"The lowest life expectancy in the dataset is  {lowest}")
print(f"The highest life expectancy in the dataset is  {highest}")
