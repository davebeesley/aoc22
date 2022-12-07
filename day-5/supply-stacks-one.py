stacking_data = open("input.txt", "r")

stacks = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]
instructions = []

line_counter = 1

for line in stacking_data:
    if line_counter < 9:
        if line[1] and line[1] != ' ':
            stacks[0].append(line[1])
        if line[5] and line[5] != ' ':
            stacks[1].append(line[5])
        if line[9] and line[9] != ' ':
            stacks[2].append(line[9])
        if line[13] and line[13] != ' ':
            stacks[3].append(line[13])
        if line[17] and line[17] != ' ':
            stacks[4].append(line[17])
        if line[21] and line[21] != ' ':
            stacks[5].append(line[21])
        if line[25] and line[25] != ' ':
            stacks[6].append(line[25])
        if line[29] and line[29] != ' ':
            stacks[7].append(line[29])
        if line[33] and line[33] != ' ':
            stacks[8].append(line[33])
    elif line_counter > 10:
        if (line[0]):
            this_instruction = line.replace('move ', '').replace('from', '').replace('to', '').split()
            instructions.append(this_instruction)
            
    line_counter += 1

for instruction in instructions:
    move_amount = int(instruction[0])
    from_stack = int(instruction[1]) - 1
    to_stack = int(instruction[2]) - 1

    for i in range(move_amount):
        if len(stacks[from_stack]) > 0:
            to_move = stacks[from_stack].pop(0)
            stacks[to_stack].insert(0, to_move)

for stack in stacks:
    print(stack[0])