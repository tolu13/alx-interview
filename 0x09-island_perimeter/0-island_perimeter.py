#!/usr/bin/python3

def island_perimeter(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                
                # Check adjacent cells
                if r > 0 and grid[r - 1][c] == 1:  # check above
                    perimeter -= 1
                if r < rows - 1 and grid[r + 1][c] == 1:  # check below
                    perimeter -= 1
                if c > 0 and grid[r][c - 1] == 1:  # check left
                    perimeter -= 1
                if c < cols - 1 and grid[r][c + 1] == 1:  # check right
                    perimeter -= 1
    
    return perimeter
