# Python program to generate a valid
# sudoku with k empty cells
# https://www.geeksforgeeks.org/program-sudoku-generator/

import random


def unUsedInBox(grid, rowStart, colStart, num):
    """Returns false if given 3x3 block contains num"""
    for i in range(3):
        for j in range(3):
            if grid[rowStart + i][colStart + j] == num:
                return False
    return True


def fillBox(grid, row, col):
    """Fill a 3x3 matrix"""
    for i in range(3):
        for j in range(3):
            while True:
                num = random.randint(1, 9)
                if unUsedInBox(grid, row, col, num):
                    break
            grid[row + i][col + j] = num


def unUsedInRow(grid, i, num):
    """Check if it's safe to put num in row i"""
    for j in range(9):
        if grid[i][j] == num:
            return False
    return True


def unUsedInCol(grid, j, num):
    """Check if it's safe to put num in column j"""
    for i in range(9):
        if grid[i][j] == num:
            return False
    return True


def checkIfSafe(grid, i, j, num):
    """Check if safe to put in cell"""
    return (unUsedInRow(grid, i, num) and
            unUsedInCol(grid, j, num) and
            unUsedInBox(grid, i - i % 3, j - j % 3, num))


def fillDiagonal(grid):
    """Fill the diagonal 3x3 matrices"""
    for i in range(0, 9, 3):
        fillBox(grid, i, i)


def fillRemaining(grid, i, j):
    """Fill remaining blocks"""
    if j >= 9 and i < 8:
        i += 1
        j = 0
    if i >= 9 and j >= 9:
        return True
    if i < 3:
        if j < 3:
            j = 3
    elif i < 6:
        if j == (i // 3) * 3:
            j += 3
    else:
        if j == 6:
            i += 1
            j = 0
            if i >= 9:
                return True

    for num in range(1, 10):
        if checkIfSafe(grid, i, j, num):
            grid[i][j] = num
            if fillRemaining(grid, i, j + 1):
                return True
            grid[i][j] = 0
    return False


def removeKDigits(grid, k):
    """Remove k digits randomly"""
    while k > 0:
        cellId = random.randint(0, 80)
        i = cellId // 9
        j = cellId % 9

        if grid[i][j] != 0:
            grid[i][j] = 0
            k -= 1


def sudokuGenerator(k):
    """Generate a Sudoku grid with k empty cells"""
    grid = [[0 for _ in range(9)] for _ in range(9)]

    fillDiagonal(grid)
    fillRemaining(grid, 0, 3)
    solution = [[x for x in grid[i]] for i in range(9)]
    removeKDigits(grid, k)
    return grid, solution


if __name__ == '__main__':
    random.seed()
    k = 20
    game, solution = sudokuGenerator(k)

    for row in game:
        print(' '.join(map(str, row)))
    print('')
    for row in solution:
        print(' '.join(map(str, row)))
