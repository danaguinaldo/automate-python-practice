#! python3
# characterGrid.py - Print picture from grid.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']] 

def printGrid(grid):
    for x in range(0, len(grid[0])):
        for y in range(len(grid)-1, -1, -1):
            print(grid[y][x], end = '')
        print('')

def main():
    printGrid(grid)

main()