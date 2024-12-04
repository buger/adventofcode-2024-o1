import sys

def main():
    # Read the grid from stdin
    grid = [line.strip() for line in sys.stdin if line.strip()]
    if not grid:
        print(0)
        return

    # Convert the grid to a list of lists for easier indexing
    grid = [list(line) for line in grid]

    # Get the dimensions of the grid
    nrows = len(grid)
    ncols = len(grid[0])

    count = 0

    # Define acceptable sequences
    valid_sequences = {'MAS', 'SAM'}

    # Iterate over the grid, excluding the borders
    for i in range(1, nrows - 1):
        for j in range(1, ncols - 1):
            # Check if diagonals are within bounds
            if (0 <= i-1 < nrows and 0 <= i+1 < nrows and
                0 <= j-1 < ncols and 0 <= j+1 < ncols):

                # Left diagonal positions
                l1 = grid[i-1][j-1]
                l2 = grid[i][j]
                l3 = grid[i+1][j+1]
                left_diag = l1 + l2 + l3

                # Right diagonal positions
                r1 = grid[i-1][j+1]
                r2 = grid[i][j]
                r3 = grid[i+1][j-1]
                right_diag = r1 + r2 + r3

                # Check if both diagonals form 'MAS' or 'SAM'
                if left_diag in valid_sequences and right_diag in valid_sequences:
                    count += 1

    print(count)

if __name__ == "__main__":
    main()
