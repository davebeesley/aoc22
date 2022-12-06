pairs = open("input.txt", "r")

overlapping = 0

for pair in pairs:
    assignments = pair.replace('\n', '').split(',')
    range_one = assignments[0].split('-')
    range_two = assignments[1].split('-')

    if int(range_one[0]) >= int(range_two[0]) and int(range_one[0]) <= int(range_two[1]):
        overlapping += 1
    elif int(range_one[1]) <= int(range_two[1]) and int(range_one[1]) >= int(range_two[0]):
        overlapping += 1
    elif int(range_two[0]) >= int(range_one[0]) and int(range_two[0]) <= int(range_one[1]):
        overlapping += 1
    elif int(range_two[1]) <= int(range_one[1]) and int(range_two[1]) >= int(range_one[0]):
        overlapping += 1

print(overlapping)