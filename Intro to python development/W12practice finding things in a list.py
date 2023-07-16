people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]


younger_age = -1
youger_person = "" # It doesn't matter what you set this to, it just needs to be declared

for item in people:
    youger_person = item[0] # Product name is the first part
    younger_age = item[1] 

    if item < younger_age :
        # This is the new max
        younger_age = younger_age

        # Also save this product name as the max product
        youger_person = younger_age

print(f"The younger age is: {younger_age}")
print(f"The younger person is: {youger_person}")