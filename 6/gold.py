import sys

# Read the map from stdin
lines = [line.rstrip('\n') for line in sys.stdin]

grid = [list(row) for row in lines]
rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

# Directions in order: up, right, down, left
directions = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

# We also need a way to turn right:
# up -> right, right -> down, down -> left, left -> up
turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

# Find the guard's starting position and direction
start_r = start_c = None
direction = None

for r in range(rows):
    for c in range(cols):
        if grid[r][c] in directions:
            start_r, start_c = r, c
            direction = grid[r][c]
            # Replace the guard symbol with '.' since it's effectively empty space after we start
            grid[r][c] = '.'
            break
    if direction:
        break

# Set for visited positions
visited = set()
visited.add((start_r, start_c))

r, c = start_r, start_c
d = direction

while True:
    # Check the cell in front of the guard
    dr, dc = directions[d]
    nr, nc = r + dr, c + dc

    # If the next position is outside the grid, stop
    if not (0 <= nr < rows and 0 <= nc < cols):
        break

    # If there is something (#) in front, turn right
    if grid[nr][nc] == '#':
        d = turn_right[d]
        # Don't move yet, just turn
        continue
    else:
        # Move forward
        r, c = nr, nc
        visited.add((r, c))

# Print the number of distinct visited positions
print(len(visited))
