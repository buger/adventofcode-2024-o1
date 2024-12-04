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

    word = 'XMAS'
    word_length = len(word)

    # Directions: N, NE, E, SE, S, SW, W, NW
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]

    count = 0

    for i in range(nrows):
        for j in range(ncols):
            for dx, dy in directions:
                k = 0
                x, y = i, j
                while k < word_length:
                    # Check boundaries
                    if 0 <= x < nrows and 0 <= y < ncols:
                        if grid[x][y] == word[k]:
                            x += dx
                            y += dy
                            k += 1
                        else:
                            break
                    else:
                        break
                if k == word_length:
                    count += 1

    print(count)

if __name__ == "__main__":
    main()
