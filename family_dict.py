# Set up the data in a dictionary
my_family = {
    'brother1': {
        'name': 'Callen',
        'age': 62
    },
    'brother2': {
        'name': 'Tim',
        'age': 61
    },
    'brother4': {
        'name': 'Michael',
        'age': 55
    },
    'brother3': {
        'name': 'Patrick',
        'age': 58
    },
    'mother': {
        'name': 'Betty',
        'age': 87
    }
}

# Create empty set
family_set = set()
# Iterate over the dictionary and add new items including name and age to a set
for family_member, member_values in my_family.items():
    family_set.add(f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old')

# Print out the family items
print("My family!", family_set)