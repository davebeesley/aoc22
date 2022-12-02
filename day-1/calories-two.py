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

top_three_calories = all_elf_calories[-1] + all_elf_calories[-2] + all_elf_calories[-3]

print(top_three_calories)