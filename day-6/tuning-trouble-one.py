datastream_buffer = open("input.txt", "r")
datastream = datastream_buffer.readline()

marker = 0

current_four_chars = []

for letter in datastream:
    if len(current_four_chars) == 4:
        if len(current_four_chars) == len(set(current_four_chars)):
            print(marker)
            exit()

        current_four_chars.pop(0)
    
    current_four_chars.append(letter)
    marker += 1