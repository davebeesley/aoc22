elves_calories = open("input.txt", "r")

all_elf_calories = []

current_elf_calories = 0

for line in elves_calories:
    if line != '\n':
        current_elf_calories += int(line)
    else:
        all_elf_calories.append(current_elf_calories)
        current_elf_calories = 0

all_elf_calories.sort()

print(all_elf_calories[-1])