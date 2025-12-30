# Read the input
input = open("day1/input.txt").read()

# Dial starts at 50, goes from 0 to 99
dial_position = 50

moves = input.splitlines()
# Part 1, count how many times the dial hits exactly 0
total_hits = 0
for move in moves:
    prev_position = dial_position
    direction, steps = move[0], int(move[1:])
    if direction == 'L':
        dial_position = (dial_position - steps) % 100  # modulus to wrap length of [0-99]
    elif direction == 'R':
        dial_position = (dial_position + steps) % 100  

    if dial_position == 0:
        total_hits += 1
print(total_hits)

# Part 2, count how many times the dial crosses 0 during a rotation
# do not include landing on 0, only crossing it
dial_position = 50

for move in moves:
    direction, steps = move[0], int(move[1:])

    while steps:
        if direction == 'L':

            if dial_position-1 == -1:
                dial_position = 99
            else:
                dial_position -= 1

        elif direction == 'R':
            
            if dial_position+1 == 100:
                dial_position = 0
            else:
                dial_position += 1

        if dial_position == 0 and steps > 1:
            total_hits += 1

        steps -= 1

print(total_hits)