# Safe with dial 0-99
# Input: Sequence of `rotations` Starts with `L` or `R` followed by rotation distance
# The dial starts by pointing at 50
# The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence

def count_zero_rotations(rotations):
    dial_position = 50 # Starting position
    zero_count = 0

    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == 'L':
            dial_position = (dial_position - distance) % 100
        elif direction == 'R':
            dial_position = (dial_position + distance) % 100

        if dial_position == 0:
            zero_count += 1

    return zero_count

if __name__ == "__main__":
    # get rotations from day1_input.txt
    with open("day1_input.txt", "r") as file:
        rotations = [line.strip() for line in file.readlines()]
    result = count_zero_rotations(rotations)
    print(f"The number of times the dial points to 0: {result}")
