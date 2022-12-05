rucksacks = open("input.txt", "r")

priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

total_priority = 0

for rucksack in rucksacks:
    compartment_one, compartment_two = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    in_both = set(compartment_one) & set(compartment_two)
    priority = priorities.index(''.join(in_both)) + 1
    total_priority += priority

print(total_priority)