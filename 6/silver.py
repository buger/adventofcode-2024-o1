import sys

lines = [line.rstrip('\n') for line in sys.stdin]
grid = [list(row) for row in lines]
rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

# Directions and turning right logic
directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

# Find guard start
start_r = start_c = None
start_d = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] in directions:
            start_r, start_c = r, c
            start_d = grid[r][c]
            grid[r][c] = '.'  # Replace with empty space now that we have the direction
            break
    if start_d:
        break

def simulate_with_obstruction(grid):
    """
    Simulates the guard's movement on the given grid until the guard either:
    - Leaves the map (returns False for no loop)
    - Enters a repeated state (returns True for loop)

    The guard always starts from (start_r, start_c) facing start_d.
    """
    r, c = start_r, start_c
    d = start_d

    visited_states = set()
    visited_states.add((r, c, d))

    while True:
        dr, dc = directions[d]
        nr, nc = r + dr, c + dc

        # If next position is outside, no loop
        if not (0 <= nr < rows and 0 <= nc < cols):
            return False

        # If obstacle ahead, turn right
        if grid[nr][nc] == '#':
            d = turn_right[d]
        else:
            # Move forward
            r, c = nr, nc

            # If we have seen this state before, it's a loop
            if (r, c, d) in visited_states:
                return True
            visited_states.add((r, c, d))

def is_valid_obstruction(r, c):
    # Cannot place obstruction at the guard's start
    if (r, c) == (start_r, start_c):
        return False

    if grid[r][c] != '.':
        return False

    # Temporarily place obstruction
    grid[r][c] = '#'
    loop_formed = simulate_with_obstruction(grid)
    # Restore
    grid[r][c] = '.'

    return loop_formed

count = 0
for r in range(rows):
    for c in range(cols):
        if is_valid_obstruction(r, c):
            count += 1

print(count)
