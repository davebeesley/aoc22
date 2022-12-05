rucksacks = open("input.txt", "r")

priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

current_elf_groups = []

total_priority = 0

for rucksack in rucksacks:
    current_elf_groups.append(rucksack.replace('\n', ''))
    
    if len(current_elf_groups) == 3:
        in_all_three = set(current_elf_groups[0]) & set(current_elf_groups[1]) & set(current_elf_groups[2])
        priority = priorities.index(''.join(in_all_three)) + 1
        total_priority += priority
        current_elf_groups = []

print(total_priority)