import re

# Remove repeating tile positions and their corresponding numbers
def distinctify(positions, numbers):
    j = 0
    while j != len(positions) - 1:
        if positions[j] == positions[j + 1]:
            del (positions[j + 1])
            del (numbers[j + 1])
        else:
            j += 1
        if j == len(positions) - 1:
            break

# Parse the tile positions and numbers from the HTML string
def parse_string_regex(string):
    regex_pos = re.compile(r'tile-position-\d-\d')
    regex_nums = re.compile(r'"tile-inner">\d')
    positions = [pos[-4:].replace('-', '') for pos in regex_pos.findall(string)]
    numbers = [num[-1] for num in regex_nums.findall(string)]

    return positions, numbers
