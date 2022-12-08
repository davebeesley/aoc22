datastream_buffer = open("input.txt", "r")
datastream = datastream_buffer.readline()

marker = 0

current_fourteen_chars = []

for letter in datastream:
    if len(current_fourteen_chars) == 14:
        if len(current_fourteen_chars) == len(set(current_fourteen_chars)):
            print(marker)
            exit()

        current_fourteen_chars.pop(0)
    
    current_fourteen_chars.append(letter)
    marker += 1