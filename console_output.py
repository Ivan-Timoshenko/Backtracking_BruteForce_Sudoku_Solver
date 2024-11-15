from dataclasses import dataclass
from time import sleep
from matrixMethods import create_matrix
from sys import stdout
import os

@dataclass
class Cell:
    row: int
    col: int
    console_row: int
    console_col: int

    def __init__(self, in_row, in_col):
        self.row, self.col = in_row, in_col
        if 0 <= self.row <= 2:
            self.console_row = self.row + 1
        elif 3 <= self.row <= 5:
            self.console_row = self.row + 2
        elif 6 <= self.row <= 8:
            self.console_row = self.row + 3
        elif self.col == -1:
            self.console_row = 4
        elif self.col == -2:
            self.console_row = 8

        if self.col == 0:
            self.console_col = 1
        elif 0 < self.col <= 2:
            self.console_col = 2*self.col+1
        elif 3 <= self.col <= 5:
            self.console_col = 2*self.col + 3
        elif 6 <= self.col <= 8:
            self.console_col = 2*self.col + 5
        elif self.col == -1:
            self.console_col = 7
        elif self.col == -2:
            self.console_col = 17

# 0<=row<=2 => row = row+1
# 3<=row<=5 => row = row+2
# 6<=row<=8 => row = row+3

# col == 0 => col = 1
# 0<col<=2 => col = 2*col+1
# 3<=col<=5 => col = 2*col + 3
# 6<=col<=8 => col = 2*col + 5
# 1 2 3 | 4 5 6 | 7 8 9
#region Windows Shenanigans
if os.name == "nt":
    import ctypes

    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
#endregion

#region Cursor mover to x: coord[0], y: coord[1]
def jump(cell: Cell) -> None:
    stdout.write(f'\033[{cell.console_row};{cell.console_col}H')
#endregion

def display_matrix(data: list[list[str]], fixes: dict[tuple[int, int], int]) -> None:
    for row in range(len(data)):
        for col in range(len(data[0])):
            box = Cell(row, col)
            if (row, col) in fixes.keys():
                stdout.write('\033[94m') #fixes are colored bright blue
            else:
                stdout.write('\033[37m') #dots are colored white
            jump(box)
            stdout.write(str(data[row][col]))
            stdout.flush()

stdout.write('\033[2J') #display cleared
stdout.write('\033[?25l') #cursor hidden


matrix, already_set = create_matrix(9, 27)

while True:
    try:
        display_matrix(matrix, already_set)
        sleep(1000000)
    except KeyboardInterrupt:
        break

stdout.write('\033[?25h') #cursor found
stdout.write('\033[37m')
stdout.flush()